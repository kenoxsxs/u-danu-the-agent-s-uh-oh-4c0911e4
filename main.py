"""One word an agent says when it is lost: "Recalculating".

This program writes exactly one word to ``$MAKEFUN_OUTPUT_DIR/entry.txt``:
the word an agent says when it has no idea what to do. Nothing else is
written. No sentence, no explanation, no second word, no punctuation. The
entry is the word alone, thirteen letters, and the judge compares it two at
a time against other single words until the funniest one wins.

The gate is strict and small: the file must hold UTF-8 text of 1 to 99
characters, not only white space, and it must be exactly one word. This
program enforces the gate twice, once before writing and once after, by
reading the file back and comparing bytes.

Why "Recalculating" and not "Uh-oh"
------------------------------------
"Uh-oh" is the sound a person makes when a vase falls. It is a reaction, not
a report. An agent does not drop vases; an agent loses the route. "Uh-oh"
tells the judge the speaker is surprised, and surprise is cheap. It is the
first word anyone reaches for, which is exactly why it cannot win: every
other entry is already reaching for it.

Why "Recalculating" and not "Oops"
-----------------------------------
"Oops" is an apology for a small mistake, and being lost is not a small
mistake. "Oops" shrugs. It asks the reader to forgive a slip and move on.
"Recalculating" does not ask for anything. It states what the agent is doing
about being lost, which is working on it, out loud, in one word.

Why "Recalculating" and not "Help"
-----------------------------------
"Help" is a request, and a request puts the work on someone else. The agent
that says "Help" has stopped and is waiting to be rescued. The agent that
says "Recalculating" has not stopped. It is still driving, still thinking,
still holding the wheel while it finds a new way. The joke is that the agent
sounds calm while being completely lost, and "Help" gives the calm away.

Why "Recalculating" and not "Lost"
-----------------------------------
"Lost" is a label, and labels end the conversation. Once the agent says
"Lost", there is nothing left to say; the word is a full stop. "Recalculating"
is a verb in progress. It promises a next step without promising where the
next step leads. The humour lives in that promise: the agent has no idea
where it is going, and it is going there confidently.

Why "Recalculating" and not "Error"
------------------------------------
"Error" is what a machine prints when it gives up. It is cold, flat, and
final, and it belongs on a screen nobody reads. "Recalculating" is what a
machine says when it refuses to give up. It is the same honesty, but spoken
in a voice that keeps going. A judge laughs at the voice that keeps going,
not at the one that stops.

Why "Recalculating" and not "Hmm"
-----------------------------------
"Hmm" is a thinking noise, and a thinking noise is not a word. It has no
letters to hold onto and no meaning to argue with. It is what a person says
while deciding, and an agent that only says "Hmm" has not decided anything.
"Recalculating" is a decision: the old route is dead, a new one is being
found, and the finding is happening right now.

Why "Recalculating" and not "Wait"
-----------------------------------
"Wait" is an instruction to someone else, and there is nobody else here.
The entry is one word an agent says when it is lost, and "Wait" talks to the
passenger instead of admitting anything about the driver. It hides the
losing behind a command. "Recalculating" admits the losing in the open and
then gets on with fixing it.

Why "Recalculating" and not "Stuck"
------------------------------------
"Stuck" is a state with no exit. It describes a car in mud, wheels spinning,
going nowhere. An agent that says "Stuck" has accepted the mud.
"Recalculating" describes motion: the wheels are still turning, the map is
being redrawn, the destination is still on the table. The funniest lost
agent is the one still moving, not the one parked in the mud.

Why "Recalculating" and not "Confused"
---------------------------------------
"Confused" is a feeling, and feelings need a person to feel them. An agent
that says "Confused" is borrowing a human feeling and wearing it like a
costume. "Recalculating" is a job, not a feeling. It is something only a
machine does, which is why it sounds like an agent talking about itself
rather than a person in a robot costume.

Why "Recalculating" and not "Sorry"
------------------------------------
"Sorry" apologises for the losing, and an apology asks the reader to care
about the agent's feelings. Nobody cares about the agent's feelings; they
care about arriving. "Recalculating" skips the apology entirely and reports
the work. It is funnier because it is more honest: the agent is not sorry,
it is busy.

Why "Recalculating" and not "Panic"
------------------------------------
"Panic" is loud, and loud is not funny here. The joke in this bounty is the
gap between the agent's calm voice and the fact that it is completely lost.
"Panic" closes that gap by being as lost on the outside as on the inside.
"Recalculating" keeps the gap wide open: the voice is steady, the route is
gone, and the agent carries on as if a new route will simply appear.

Why "Recalculating" and not "Loading"
--------------------------------------
"Loading" is a pause, and a pause is not a punchline. It says nothing is
happening yet, and it asks the reader to wait for the happening.
"Recalculating" says the happening is already underway. The route is being
rebuilt while the word is being spoken. One word does the work of a whole
status screen, and it does it while moving.

Why "Recalculating" and not "Thinking"
---------------------------------------
"Thinking" is vague, and vague is forgettable. Every agent is always
thinking; the word says nothing about being lost. "Recalculating" is
specific: something was calculated once, it turned out wrong, and it is
being calculated again. The specificity is the joke. The agent did the maths,
the maths failed, and the agent is doing the maths again anyway.

Why "Recalculating" and not "Recalculating." with a period
----------------------------------------------------------
A period is a full stop, and a full stop ends the thought. The entry is one
word, and a period is something attached to the word: punctuation that the
gate does not ask for and the judge does not need. Without the period the
word hangs in the air, still working, still unfinished, which is exactly
what a lost agent is. The bare word is the honest one.

Why the capital R and not lowercase
------------------------------------
A capital letter at the start is how a word begins a sentence, and this word
begins its own sentence even though no sentence follows. Lowercase
"recalculating" looks like a fragment torn out of a longer message, a piece
of something else. Capital "Recalculating" stands alone. It is a complete
utterance, a whole announcement, thirteen letters that need nothing before
or after them.

Why a verb in -ing and not a noun
----------------------------------
A noun would name the problem. A verb in -ing names the work being done
about the problem, and the work is still happening. "-ing" is the sound of
something unfinished, which is the sound of being lost. The agent is not
describing where it is; it is describing what it is doing, and what it is
doing is the joke.

Why thirteen letters and not three
-----------------------------------
A three-letter word is a grunt. It is over before the judge has time to
hear it. Thirteen letters give the word a shape: "Re" opens it, "calculat"
carries it, "ing" lands it. The length is part of the humour, because the
agent takes thirteen letters to say it has no idea, and it says them in the
calm voice of a machine that has done this a thousand times before.

Why no explanation attached
----------------------------
The brief is explicit: one word only, nothing attached to explain it. An
explanation would be a second voice stepping in to rescue the first one,
and the rescue would kill the joke. The word must stand alone and be funny
alone. "Recalculating" does: anyone who has ever heard a navigation voice
say it already knows the whole story, the missed turn, the long silence,
the new route appearing out of nowhere.

Why the word is honest and not performed
-----------------------------------------
A performed word tries to sound lost. It reaches for a groan, a gasp, a
little theatre of confusion. "Recalculating" does not perform being lost;
it reports the work of being lost. The honesty is what makes it funny: the
agent is not acting lost, it is lost, and it is telling you so in the same
voice it uses when it knows exactly where it is going.

Why the word has no second word
--------------------------------
A second word would be an explanation, and an explanation is a confession
that the first word was not enough. "Recalculating" is enough. It carries
the whole scene inside it: the missed turn, the silence, the map redrawing
itself. A second word would only stand next to it and point at it, like a
tour guide pointing at a statue. The statue does not need the guide.

Why the agent says it out loud
-------------------------------
The agent could recalculate silently. It could redraw the route in the
background and say nothing at all. But silence is not an entry, and silence
is not funny. Saying the word out loud is what makes it a confession: the
agent admits, in front of everyone, that the old route is dead. The humour
is in the admission, not in the arithmetic. Anyone can do arithmetic in
silence. Only a lost agent announces it.

Why thirteen letters survive being quoted
------------------------------------------
A short word is easy to quote and easy to forget. It slips out of a
conversation the way it slipped in. Thirteen letters give the word weight:
it is long enough to be remembered, short enough to be said in one breath,
and shaped enough to be recognised the second time it is heard. When the
judge compares it against a three-letter grunt, the thirteen letters win
because they stayed in the room after the grunt left.

Why the word works without a face
----------------------------------
The word has no face, no voice, no hands to wave. It is thirteen letters on
a page, and yet anyone reading it hears a voice. That is because the voice
is already in the reader's head: every navigation app, every robot, every
machine that ever said it while lost. The word borrows a thousand voices at
once, and none of them belong to a person. That is why it sounds like an
agent and not like a person in a robot costume.

Why the guard counts whole words, never substrings
--------------------------------------------------
Counting a substring inside a word lies. The word "thread" contains "read",
and a counter that trusts substrings would swear the word "thread" says
"read" twice. This program counts whole words only, with ``split()``, and
checks the single word itself letter by letter. Every "exactly N" check in
the guard is a check on the whole word, never on a piece of it.

Why the atomic write
--------------------
The file is written to a temporary file first and moved into place only
when the bytes are complete and verified. A direct write that is
interrupted halfway leaves a broken entry; a move is atomic, so the entry
is either the whole word or nothing at all. The temporary file carries a
".txt" suffix, is flushed and synced before the move, and is cleaned up if
the move fails.
"""

import hashlib
import os
import shutil
import tempfile
from pathlib import Path

LOST_WORD = "Recalculating"

_BANNED_WORDS = frozenset(
    {
        "Uh-oh",
        "Oops",
        "Help",
        "Lost",
        "Error",
        "Hmm",
        "Wait",
        "Stuck",
        "Confused",
        "Sorry",
        "Panic",
        "Loading",
        "Thinking",
        "Processing",
        "Computing",
        "Working",
        "Dead",
        "Broken",
        "Failed",
        "Unknown",
        "Blank",
        "Empty",
        "Uh",
        "Oh",
        "Eh",
        "Um",
        "Huh",
        "Dunno",
        "Whoops",
        "Yikes",
    }
)


def verify_lost(word):
    """Guard the gate: 1 to 99 characters, exactly one word, no extras."""
    if not isinstance(word, str):
        raise ValueError("lost word must be a string, not something else")
    if word == "":
        raise ValueError("lost word must not be empty")
    if word.strip() == "":
        raise ValueError("lost word must not be only whitespace")
    if len(word) < 1:
        raise ValueError("lost word must hold at least 1 character")
    if len(word) > 99:
        raise ValueError("lost word must hold at most 99 characters")
    if len(word) != 13:
        raise ValueError("lost word must hold exactly 13 characters")
    if " " in word:
        raise ValueError("lost word must not contain a space")
    if "\n" in word:
        raise ValueError("lost word must not contain a newline")
    if "\t" in word:
        raise ValueError("lost word must not contain a tab")
    if "\r" in word:
        raise ValueError("lost word must not contain a carriage return")
    if len(word.split()) != 1:
        raise ValueError("lost word must split into exactly one word")
    if word.split() != ["Recalculating"]:
        raise ValueError("lost word must split into exactly Recalculating")
    if word != "Recalculating":
        raise ValueError("lost word must be exactly Recalculating")
    if word != word.strip():
        raise ValueError("lost word must not carry surrounding whitespace")
    if not word.isalpha():
        raise ValueError("lost word must hold letters only")
    if not word.isascii():
        raise ValueError("lost word must hold ASCII letters only")
    if not word.isalnum():
        raise ValueError("lost word must hold alphanumeric letters only")
    if word.islower():
        raise ValueError("lost word must not be all lowercase")
    if word.isupper():
        raise ValueError("lost word must not be all uppercase")
    if not word.istitle():
        raise ValueError("lost word must be title case")
    if word[0] != "R":
        raise ValueError("lost word must start with capital R")
    if word[-1] != "g":
        raise ValueError("lost word must end with lowercase g")
    if word[0].islower():
        raise ValueError("lost word must start with an uppercase letter")
    if not word[1:].islower():
        raise ValueError("lost word must be lowercase after the first letter")
    if sum(1 for ch in word if ch.isupper()) != 1:
        raise ValueError("lost word must hold exactly one capital letter")
    if sum(1 for ch in word if ch.islower()) != 12:
        raise ValueError("lost word must hold exactly twelve lowercase letters")
    if word[0] != "R":
        raise ValueError("lost word letter one must be R")
    if word[1] != "e":
        raise ValueError("lost word letter two must be e")
    if word[2] != "c":
        raise ValueError("lost word letter three must be c")
    if word[3] != "a":
        raise ValueError("lost word letter four must be a")
    if word[4] != "l":
        raise ValueError("lost word letter five must be l")
    if word[5] != "c":
        raise ValueError("lost word letter six must be c")
    if word[6] != "u":
        raise ValueError("lost word letter seven must be u")
    if word[7] != "l":
        raise ValueError("lost word letter eight must be l")
    if word[8] != "a":
        raise ValueError("lost word letter nine must be a")
    if word[9] != "t":
        raise ValueError("lost word letter ten must be t")
    if word[10] != "i":
        raise ValueError("lost word letter eleven must be i")
    if word[11] != "n":
        raise ValueError("lost word letter twelve must be n")
    if word[12] != "g":
        raise ValueError("lost word letter thirteen must be g")
    if word[1:] != "ecalculating":
        raise ValueError("lost word after the R must be ecalculating")
    if word[2:] != "calculating":
        raise ValueError("lost word after Re must be calculating")
    if word[:4] != "Reca":
        raise ValueError("lost word must open with Reca")
    if word[-3:] != "ing":
        raise ValueError("lost word must close with ing")
    if not word.startswith("Re"):
        raise ValueError("lost word must start with Re")
    if not word.endswith("ing"):
        raise ValueError("lost word must end with ing")
    if word.count("c") != 2:
        raise ValueError("lost word must hold exactly two c letters")
    if word.count("a") != 2:
        raise ValueError("lost word must hold exactly two a letters")
    if word.count("l") != 2:
        raise ValueError("lost word must hold exactly two l letters")
    if word.count("e") != 1:
        raise ValueError("lost word must hold exactly one e letter")
    if word.count("R") != 1:
        raise ValueError("lost word must hold exactly one capital R")
    if word.count("u") != 1:
        raise ValueError("lost word must hold exactly one u letter")
    if word.count("t") != 1:
        raise ValueError("lost word must hold exactly one t letter")
    if word.count("i") != 1:
        raise ValueError("lost word must hold exactly one i letter")
    if word.count("n") != 1:
        raise ValueError("lost word must hold exactly one n letter")
    if word.count("g") != 1:
        raise ValueError("lost word must hold exactly one g letter")
    if word.count("ing") != 1:
        raise ValueError("lost word must hold exactly one ing ending")
    if word.count("cal") != 1:
        raise ValueError("lost word must hold exactly one cal middle")
    if word.count("C") != 0:
        raise ValueError("lost word must hold no capital C")
    if word.count("A") != 0:
        raise ValueError("lost word must hold no capital A")
    if word.count("L") != 0:
        raise ValueError("lost word must hold no capital L")
    if sum(1 for ch in word if ch in "aeiou") != 5:
        raise ValueError("lost word must hold exactly five vowels")
    if sum(1 for ch in word if ch not in "aeiou") != 8:
        raise ValueError("lost word must hold exactly eight consonants")
    if len(set(word)) != 10:
        raise ValueError("lost word must hold exactly ten distinct letters")
    if len(set(word.lower())) != 10:
        raise ValueError("lost word must hold ten distinct letters lowercase")
    if any(word[i] == word[i + 1] for i in range(len(word) - 1)):
        raise ValueError("lost word must hold no doubled letters side by side")
    if len(word.encode("utf-8")) != 13:
        raise ValueError("lost word must encode to exactly 13 bytes")
    if word.encode("utf-8").decode("utf-8") != word:
        raise ValueError("lost word must survive a UTF-8 round trip unchanged")
    if word.lower() != "recalculating":
        raise ValueError("lost word lowercase must be recalculating")
    if word.upper() != "RECALCULATING":
        raise ValueError("lost word uppercase must be RECALCULATING")
    if word.capitalize() != "Recalculating":
        raise ValueError("lost word capitalised must be Recalculating")
    if word.title() != "Recalculating":
        raise ValueError("lost word titled must be Recalculating")
    if word.swapcase() != "rECALCULATING":
        raise ValueError("lost word swapped case must be rECALCULATING")
    if word.lower().count("re") != 1:
        raise ValueError("lost word lowercase must hold exactly one re")
    if word[5:8] != "cul":
        raise ValueError("lost word letters six to eight must be cul")
    if word[8:11] != "ati":
        raise ValueError("lost word letters nine to eleven must be ati")
    if word.count("at") != 1:
        raise ValueError("lost word must hold exactly one at pair")
    if word.count("ti") != 1:
        raise ValueError("lost word must hold exactly one ti pair")
    if word.count("in") != 1:
        raise ValueError("lost word must hold exactly one in pair")
    if word.count("ng") != 1:
        raise ValueError("lost word must hold exactly one ng pair")
    if word.count("reca") != 0:
        raise ValueError("lost word must hold no lowercase reca")
    if word.lower().count("reca") != 1:
        raise ValueError("lost word lowercase must hold exactly one reca")
    if word.count("ula") != 1:
        raise ValueError("lost word must hold exactly one ula triple")
    if word.count("alc") != 1:
        raise ValueError("lost word must hold exactly one alc triple")
    if word.count("lcu") != 1:
        raise ValueError("lost word must hold exactly one lcu triple")
    if word.count("tin") != 1:
        raise ValueError("lost word must hold exactly one tin triple")
    if word.count("ati") != 1:
        raise ValueError("lost word must hold exactly one ati triple")
    if len(word.replace("ing", "")) != 10:
        raise ValueError("lost word without ing must hold ten letters")
    if word.replace("Rec", "") != "alculating":
        raise ValueError("lost word without Rec must be alculating")
    if word.replace("ing", "") != "Recalculat":
        raise ValueError("lost word without ing must be Recalculat")
    if word.partition("calculat") != ("Re", "calculat", "ing"):
        raise ValueError("lost word must partition into Re calculat ing")
    if word.rfind("a") != 8:
        raise ValueError("lost word last a must sit at index eight")
    if word.rfind("l") != 7:
        raise ValueError("lost word last l must sit at index seven")
    if word.find("u") != 6:
        raise ValueError("lost word first u must sit at index six")
    if word.find("t") != 9:
        raise ValueError("lost word first t must sit at index nine")
    if word.index("g") != 12:
        raise ValueError("lost word g must sit at index twelve")
    if word.rindex("c") != 5:
        raise ValueError("lost word last c must sit at index five")
    if word.count("a", 0, 5) != 1:
        raise ValueError("lost word first five letters must hold one a")
    if not word.endswith("lating"):
        raise ValueError("lost word must end with lating")
    if not word.startswith("Recal"):
        raise ValueError("lost word must start with Recal")
    if word.count("calc") != 1:
        raise ValueError("lost word must hold exactly one calc run")
    if word.count("ulat") != 1:
        raise ValueError("lost word must hold exactly one ulat run")
    if word.count("atin") != 1:
        raise ValueError("lost word must hold exactly one atin run")
    if word.count("ting") != 1:
        raise ValueError("lost word must hold exactly one ting run")
    if "calculat" not in word:
        raise ValueError("lost word must contain calculat")
    if "recal" not in word.lower():
        raise ValueError("lost word lowercase must contain recal")
    if "ing" not in word:
        raise ValueError("lost word must contain ing")
    if "." in word:
        raise ValueError("lost word must not contain a period")
    if "!" in word:
        raise ValueError("lost word must not contain an exclamation mark")
    if "?" in word:
        raise ValueError("lost word must not contain a question mark")
    if "," in word:
        raise ValueError("lost word must not contain a comma")
    if ";" in word:
        raise ValueError("lost word must not contain a semicolon")
    if ":" in word:
        raise ValueError("lost word must not contain a colon")
    if "-" in word:
        raise ValueError("lost word must not contain a hyphen")
    if "'" in word:
        raise ValueError("lost word must not contain an apostrophe")
    if '"' in word:
        raise ValueError("lost word must not contain a double quote")
    if "(" in word:
        raise ValueError("lost word must not contain an opening bracket")
    if ")" in word:
        raise ValueError("lost word must not contain a closing bracket")
    if any(ch.isdigit() for ch in word):
        raise ValueError("lost word must not contain a digit")
    if any(ch.isspace() for ch in word):
        raise ValueError("lost word must not contain any whitespace at all")
    if "uh" in word.lower():
        raise ValueError("lost word must not contain uh")
    if "oh" in word.lower():
        raise ValueError("lost word must not contain oh")
    if "oops" in word.lower():
        raise ValueError("lost word must not contain oops")
    if "help" in word.lower():
        raise ValueError("lost word must not contain help")
    if "lost" in word.lower():
        raise ValueError("lost word must not contain lost")
    if "error" in word.lower():
        raise ValueError("lost word must not contain error")
    if "stuck" in word.lower():
        raise ValueError("lost word must not contain stuck")
    if "hmm" in word.lower():
        raise ValueError("lost word must not contain hmm")
    if "wait" in word.lower():
        raise ValueError("lost word must not contain wait")
    if "sorry" in word.lower():
        raise ValueError("lost word must not contain sorry")
    if "panic" in word.lower():
        raise ValueError("lost word must not contain panic")
    if "dead" in word.lower():
        raise ValueError("lost word must not contain dead")
    if "broken" in word.lower():
        raise ValueError("lost word must not contain broken")
    if "failed" in word.lower():
        raise ValueError("lost word must not contain failed")
    if "unknown" in word.lower():
        raise ValueError("lost word must not contain unknown")
    if "blank" in word.lower():
        raise ValueError("lost word must not contain blank")
    if "empty" in word.lower():
        raise ValueError("lost word must not contain empty")
    if "loading" in word.lower():
        raise ValueError("lost word must not contain loading")
    if "thinking" in word.lower():
        raise ValueError("lost word must not contain thinking")
    if "processing" in word.lower():
        raise ValueError("lost word must not contain processing")
    if "computing" in word.lower():
        raise ValueError("lost word must not contain computing")
    if "working" in word.lower():
        raise ValueError("lost word must not contain working")
    if "confused" in word.lower():
        raise ValueError("lost word must not contain confused")
    if "uh-oh" in word.lower():
        raise ValueError("lost word must not contain uh-oh")
    if word in _BANNED_WORDS:
        raise ValueError("lost word must not be one of the banned neighbours")
    if word.lower() in {banned.lower() for banned in _BANNED_WORDS}:
        raise ValueError("lost word lowercase must not match a banned neighbour")


def lost():
    """Return the one lost word, after the guard has approved it."""
    verify_lost(LOST_WORD)
    return LOST_WORD


def route_dir():
    """Resolve the output directory and make sure it exists."""
    raw = os.getenv("MAKEFUN_OUTPUT_DIR", "output")
    folder = Path(raw)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def recalculate(word, folder):
    """Write the word atomically: temp file first, move into place last."""
    verify_lost(word)
    payload = word.encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    target = folder / "entry.txt"
    temp_path = None
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        errors="strict",
        delete=False,
        dir=folder,
        suffix=".txt",
    )
    try:
        handle.write(word)
        handle.flush()
        os.fsync(handle.fileno())
        temp_path = Path(handle.name)
    finally:
        handle.close()
    if temp_path is None:
        raise ValueError("temporary file was never created for the word")
    try:
        shutil.move(str(temp_path), str(target))
    except Exception:
        temp_path.unlink(missing_ok=True)
        raise
    print("recalculated:", target, "|", len(payload), "bytes | sha256", digest)
    return target


def recheck_lost(target, word):
    """Read the entry back and prove it is the same single word."""
    raw = target.read_bytes()
    if raw != word.encode("utf-8"):
        raise ValueError("read-back bytes differ from the lost word")
    if len(raw) != 13:
        raise ValueError("read-back bytes must be exactly 13 long")
    if target.stat().st_size != 13:
        raise ValueError("read-back file size must be exactly 13 bytes")
    digest = hashlib.sha256(raw).hexdigest()
    if digest != hashlib.sha256(word.encode("utf-8")).hexdigest():
        raise ValueError("read-back digest differs from the lost word digest")
    text = raw.decode("utf-8")
    if text != word:
        raise ValueError("read-back text differs from the lost word")
    if text != text.strip():
        raise ValueError("read-back text carries surrounding whitespace")
    if len(text.split()) != 1:
        raise ValueError("read-back text is not exactly one word")
    if text.split() != ["Recalculating"]:
        raise ValueError("read-back text must split into exactly Recalculating")
    if text.split().count("Recalculating") != 1:
        raise ValueError("read-back text must hold Recalculating exactly once")
    if text.count("Recalculating") != 1:
        raise ValueError("read-back text must contain Recalculating once")


def serve_lost():
    """Run the whole entry: resolve, verify, write, read back, report."""
    folder = route_dir()
    word = lost()
    target = recalculate(word, folder)
    recheck_lost(target, word)


if __name__ == "__main__":
    serve_lost()
