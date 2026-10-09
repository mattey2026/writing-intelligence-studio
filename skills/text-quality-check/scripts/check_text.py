#!/usr/bin/env python3
"""Readability, style and originality checks for a draft.

Standard library only. Reads local files and prints a report; sends nothing.

Usage:
    python3 check_text.py draft.md [--level General] [--sources a.txt b.txt] [--json]
"""
import argparse
import json
import re
import sys

LEVELS = {"Plain": 65, "General": 55, "Professional": 45, "Specialist": 30}

AI_PATTERNS = [
    (r"\bdelv(e|es|ing)\b", "delve"),
    (r"\btapestry\b", "tapestry"),
    (r"\btestament to\b", "testament to"),
    (r"\bin today's\b", "in today's ..."),
    (r"\bin an era of\b", "in an era of"),
    (r"\bit'?s (important|worth) (to note|noting)\b", "it's important / worth noting"),
    (r"\bnavigat\w* (the )?(complexit\w*|landscape)", "navigate the complexities"),
    (r"\bgame[- ]changer\b", "game-changer"),
    (r"\bunlock\w*\b", "unlock"),
    (r"\bharness\w*\b", "harness"),
    (r"\bseamless\w*\b", "seamless"),
    (r"\brobust\b", "robust"),
    (r"\bleverag\w*\b", "leverage"),
    (r"\bin the realm of\b", "in the realm of"),
    (r"\bever-(evolving|changing)\b", "ever-evolving"),
    (r"\ba myriad of\b", "a myriad of"),
    (r"\bplays? an? (crucial|pivotal|vital|key) role\b", "plays a crucial role"),
    (r"(^|[.!?]\s+)(furthermore|moreover|additionally),", "Furthermore / Moreover"),
    (r"\bin conclusion\b", "in conclusion"),
    (r"\blet'?s dive\b|\bdive (deep )?in(to)?\b", "let's dive in"),
    (r"\bhere'?s the thing\b", "here's the thing"),
    (r"\bat the end of the day\b", "at the end of the day"),
    (r"\bin essence\b", "in essence"),
    (r"\bembark\w*\b", "embark"),
    (r"\belevat\w*\b", "elevate"),
    (r"\bfoster\w*\b", "foster"),
    (r"\bparadigm shift\b", "paradigm shift"),
    (r"\bcutting-edge\b", "cutting-edge"),
    (r"\btransformative\b", "transformative"),
    (r"\bit'?s not (just )?[^.?!]{1,50}(,|\u2014) it'?s\b", "It's not X, it's Y"),
    (r"\bnot (just|only) [^.?!]{1,50}, but\b", "not just X, but Y"),
]


def plain_text(md):
    """Strip Markdown structure that shouldn't count toward readability."""
    md = re.sub(r"```[\s\S]*?```", " ", md)
    keep = []
    for line in md.split("\n"):
        s = line.strip()
        if re.match(r"^#{1,6}\s", s) or s.startswith("|") or re.match(r"^https?://", s) or s.startswith("*Video:"):
            continue
        keep.append(line)
    t = "\n".join(keep)
    t = re.sub(r"\[S\d+\]|\[needs source\]|\[Add your own example:[^\]]*\]", "", t, flags=re.I)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"^\s*([-*]|\d+\.)\s+", "", t, flags=re.M)
    return re.sub(r"[*_`>#]+", "", t)


def sentences(text):
    text = re.sub(r"\n{2,}", " \u00b6 ", text).replace("\n", " ")
    parts = re.split(r"(?<=[.!?])\s+|\s\u00b6\s", text)
    return [p.replace("\u00b6", "").strip() for p in parts if len(p.split()) >= 3]


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]{1,2}", w)
    return max(1, len(groups))


def normalise(text):
    text = re.sub(r"[\"\u201c][^\"\u201d]{1,400}[\"\u201d]", " ", text)  # quoted text is allowed
    text = re.sub(r"[^a-z0-9\s']", " ", text.lower())
    return text.split()


def copied_passages(draft, sources, n=8):
    body = normalise(draft)
    hits = []
    for label, text in sources:
        ref = normalise(text)
        grams = {" ".join(ref[i:i + n]) for i in range(len(ref) - n + 1)}
        i = 0
        while i + n <= len(body):
            if " ".join(body[i:i + n]) in grams:
                j = i + n
                while j < len(body) and " ".join(body[j - n + 1:j + 1]) in grams:
                    j += 1
                hits.append({"source": label, "words": j - i, "text": " ".join(body[i:j])})
                i = j
            else:
                i += 1
    copied = sum(h["words"] for h in hits)
    return hits, round(copied / max(1, len(body)) * 100, 1)


def analyse(md, level="General", sources=()):
    text = plain_text(md)
    sents = sentences(text)
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    nw, ns = max(1, len(words)), max(1, len(sents))
    syl = sum(syllables(w) for w in words)
    asl, asw = len(words) / ns, syl / nw
    ease = round(206.835 - 1.015 * asl - 84.6 * asw)
    grade = max(0.0, round(0.39 * asl + 11.8 * asw - 15.59, 1))
    long_s = [s for s in sents if len(s.split()) > 30]
    passive = [s for s in sents if re.search(r"\b(am|is|are|was|were|be|been|being)\s+(\w+ly\s+)?\w+(ed|en)\b", s, re.I)]
    patterns = []
    for rx, label in AI_PATTERNS:
        count = len(re.findall(rx, md, flags=re.I | re.M))
        if count:
            patterns.append({"pattern": label, "count": count})
    dashes = len(re.findall(r"\u2014|\u2013| -- ", md))
    openers = {}
    for s in sents:
        m = re.match(r"[A-Za-z']+", s)
        if m:
            w = m.group(0).lower()
            openers[w] = openers.get(w, 0) + 1
    rep_open = sorted(((w, c) for w, c in openers.items() if c >= 4 and c / ns > 0.08 and w not in ("the", "a", "i")), key=lambda x: -x[1])
    paras = [p for p in re.split(r"\n{2,}", md) if not re.match(r"^\s*(#|[-*]\s|\d+\.|\||```)", p)]
    long_paras = sum(1 for p in paras if len(sentences(plain_text(p))) > 5)
    hits, pct = copied_passages(md, sources) if sources else ([], 0.0)
    target = LEVELS.get(level, 55)
    return {
        "level": level,
        "target_reading_ease": target,
        "words": len(words),
        "sentences": len(sents),
        "reading_ease": ease,
        "on_target": ease >= target,
        "grade_level": grade,
        "avg_sentence_length": round(asl, 1),
        "long_sentences": long_s,
        "passive_share_pct": round(len(passive) / ns * 100),
        "ai_style_patterns": patterns,
        "dashes_per_1000_words": round(dashes / nw * 1000, 1),
        "repetitive_openings": [{"word": w, "count": c} for w, c in rep_open],
        "over_long_paragraphs": long_paras,
        "copied_passages": hits,
        "copied_share_pct": pct,
        "sources_checked": len(sources),
    }


def report(r):
    ok = lambda b: "OK " if b else "FIX"
    out = [
        f"Readability ({r['level']} target: reading ease {r['target_reading_ease']}+)",
        f"  [{ok(r['on_target'])}] Reading ease: {r['reading_ease']}   Grade level: {r['grade_level']}",
        f"  [{ok(r['avg_sentence_length'] <= 22)}] Average sentence length: {r['avg_sentence_length']} words (aim 14-20)",
        f"  [{ok(len(r['long_sentences']) <= 0.08 * max(1, r['sentences']))}] Sentences over 30 words: {len(r['long_sentences'])} of {r['sentences']}",
        f"  [{ok(r['passive_share_pct'] <= 15)}] Passive voice: {r['passive_share_pct']}% of sentences (keep under 15%)",
        f"  [{ok(r['dashes_per_1000_words'] <= 4)}] Dashes per 1,000 words: {r['dashes_per_1000_words']}",
        f"  [{ok(r['over_long_paragraphs'] == 0)}] Paragraphs over 5 sentences: {r['over_long_paragraphs']}",
        "",
        "AI-style patterns: " + (", ".join(f"{p['pattern']} x{p['count']}" for p in r["ai_style_patterns"]) or "none found"),
        "Repetitive openings: " + (", ".join(f"\"{o['word']}\" x{o['count']}" for o in r["repetitive_openings"]) or "none"),
    ]
    if r["long_sentences"]:
        out += ["", "Longest sentences:"] + [f"  - {s[:200]}" for s in sorted(r["long_sentences"], key=len, reverse=True)[:3]]
    out.append("")
    if not r["sources_checked"]:
        out.append("Originality: no source files given, so nothing was compared.")
    elif r["copied_passages"]:
        out.append(f"Originality: {len(r['copied_passages'])} copied passage(s), {r['copied_share_pct']}% of the text:")
        out += [f"  - \"...{h['text']}...\" (matches {h['source']})" for h in r["copied_passages"][:10]]
    else:
        out.append(f"Originality: no copied wording found against {r['sources_checked']} source file(s).")
    out.append("Note: the originality check covers only the files provided, not the internet.")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Readability, style and originality check for a draft.")
    ap.add_argument("draft", help="Markdown or text file to check")
    ap.add_argument("--level", default="General", choices=list(LEVELS))
    ap.add_argument("--sources", nargs="*", default=[], help="Source or earlier-draft text files to compare against")
    ap.add_argument("--json", action="store_true", help="Print JSON instead of a text report")
    a = ap.parse_args(argv)
    with open(a.draft, encoding="utf-8") as f:
        md = f.read()
    srcs = []
    for path in a.sources:
        with open(path, encoding="utf-8") as f:
            srcs.append((path, f.read()))
    r = analyse(md, a.level, srcs)
    print(json.dumps(r, indent=2) if a.json else report(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
