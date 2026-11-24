# The question bank: how it is written

The 1,033-question bank that shipped before this rebuild was 84 per cent machine-generated:
a script pasted rule text into the options and asked the candidate to recognise it. Worse, a
function called `balance_lengths()` appended each distractor's reasoning *to the option text*
so that the right answer would not look longest. That is where the strings like
"…and — It is the text of a different provision of these rules" came from.

That generator is deleted. This directory now builds the bank from hand-authored questions.

## The rule

Every question is written by hand, one at a time, against the rule text. `authoring.py`
holds the schema and the validator; `engine.py` validates and writes `questions.json`.

An option is a bare answer. It never carries reasoning. The reasoning goes in the
explanation, built from each option's own recorded "why". That separation is enforced:

    BANNED_OPT matches reasoning leaking into an option and fails the build.

## What the validator refuses

- a duplicate stem
- a stem that asks the candidate to recognise printed text
- an option over 170 characters (a quote, not an answer)
- an option ending mid-sentence
- an option containing its own reason
- two identical options
- a key that is the unique longest option
- a rationale under 80 characters
- a question with no trap and no provision coverage

The validator has rejected my own writing many times. It is not decorative.

## Coverage, while the bank is being rebuilt

`COMPLETE` in the build directory is absent while authoring is in progress. In that state
`audit.py` reports coverage as progress rather than failing on it. When the last bank is
written, create `COMPLETE` and coverage becomes a hard gate again.

## Authoring order

    bank_ch1    Chapter I-II    commencement, application, definitions, claims, conduct
    bank_ch2    Chapter II      withholding, commercial employment
    bank_ch3    Chapter III-V   qualifying service, emoluments, classes of pension
    bank_ch4    Chapter VI-IX   retirement, regulation, family pension, dearness relief
    bank_ch5    Chapter X-XIV   processing, death in service, payment

`banks.py` imports them in order.
