# The Numerical Set — worked solutions

*Every question in this file that turns on a rupee, with its matrix column, its step-by-step solution, and a note on where each wrong option comes from. Generated from the same records that build the platform, so the two cannot drift apart.*

## Q1. [PY-001] A servant's existing basic pay on 1 January 2016 is ₹12,560 in Grade Pay ₹2,400 (Level 4). What is his pay in the revised pay structure?

*Level 4 — cell:* 7 | 8 | 9 | 10 | 11 | 12
*Pay:* ₹30,500 | ₹31,400 | ₹32,300 | ₹33,300 | ₹34,300 | ₹35,300

- (A) ₹32,300, at cell 9 of Level 4 **← answer**
- (B) ₹31,400, at cell 8 of Level 4
- (C) ₹32,400, reached by rounding ₹32,279 up to the next ₹100 and reading that as the pay
- (D) ₹32,279, at cell 8 of Level 4

**Answer: (A)**

**Stepwise solution**

1. Multiply the existing basic pay by the fitment factor: 12,560 × 2.57 = 32,279.20, and rule 7(1)(A)(i) rounds this to the nearest rupee, so ₹32,279.
2. Now locate ₹32,279 in Level 4. It is not a printed cell: cell 8 is ₹31,400 and cell 9 is ₹32,300. The rule takes the pay at the cell EQUAL to the figure if there is one, and otherwise at the IMMEDIATE NEXT HIGHER cell.
3. So the pay is fixed at ₹32,300, cell 9. The ₹21 by which the cell exceeds the product is not an error and is not recovered; the rule deliberately lands the servant on the next higher cell so that nobody loses by the conversion.

**Why the other options are wrong**

- B — That is the cell BELOW the product — the opposite of where the rule goes, since the pay must be equal to or above the product.
- C — There is no rounding of the product to ₹100. Rule 7(1)(A)(i) rounds to the rupee and then LOCATES the figure; the cell happens to be ₹32,300 here, but it is reached by location, not by rounding.
- D — ₹32,279 is the product, and it is not a cell of Level 4 at all. Rule 7(1)(A)(i) does not fix pay at the product; it locates it in the matrix and takes the equal or next higher cell — and cell 8, ₹31,400, lies below it.

**Exam-safe point: 2.57 → round to the rupee → equal or next higher cell. Never a lower cell.**

> *Authority:* Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016 (the gazette's own illustration)

---

## Q2. [PY-002] Existing basic pay ₹8,000 in Level 1 on 1 January 2016. The product of ₹20,560 is not itself a cell. What is the revised pay?

*Level 1 — cell:* 4 | 5 | 6 | 7 | 8
*Pay:* ₹19,700 | ₹20,300 | ₹20,900 | ₹21,500 | ₹22,100

- (A) ₹20,300, at cell 5 of Level 1
- (B) ₹20,900, at cell 6 of Level 1 **← answer**
- (C) ₹24,000, at cell 13 of Level 1
- (D) ₹20,560, because the product came out to a whole rupee

**Answer: (B)**

**Stepwise solution**

1. 8,000 × 2.57 = 20,560 exactly, with no rounding to do.
2. Look for 20,560 in Level 1: cell 5 is ₹20,300 and cell 6 is ₹20,900. There is no cell of ₹20,560, so the rule takes the immediate next higher cell.
3. Pay is fixed at ₹20,900, cell 6. The fact that the multiplication came out to a whole rupee does not help — what matters is whether that rupee figure is a printed cell, and 20,560 is not.

**Why the other options are wrong**

- A — That cell is BELOW the product, and the rule never moves down to reach a cell.
- C — That is 8,000 × 3, not 8,000 × 2.57. The fitment factor is 2.57, not 3.
- D — A whole-rupee product is not itself a cell. Only the 543 figures printed in the matrix are cells, and 20,560 is not one of them.

**Exam-safe point: Product 20,560 is not a cell. Cell 6 is ₹20,900 — next higher, not nearest.**

> *Authority:* Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016

---

## Q3. [PY-003] Existing basic pay ₹6,000 in Level 1 on 1 January 2016. The first cell of Level 1 is ₹18,000. What is the revised pay?

*Level 1 — cell:* 1 | 2 | 3 | 4
*Pay:* ₹18,000 | ₹18,500 | ₹19,100 | ₹19,700

- (A) ₹16,000, the rounded product, with personal pay for the rest of the gap
- (B) ₹15,420, the product itself, because clause (i) is the only operative provision here
- (C) ₹18,000, the first cell **← answer**
- (D) ₹15,500, the cell nearest the product

**Answer: (C)**

**Stepwise solution**

1. 6,000 × 2.57 = 15,420.
2. 15,420 is below the first cell of Level 1, which is ₹18,000. Rule 7(1)(A)(ii) deals with exactly this case: if the minimum pay or first cell is MORE than the amount arrived at under clause (i), the pay is fixed at that first cell.
3. So the pay is ₹18,000, cell 1. The rule does not leave him at 15,420 and it does not create an intermediate cell.

**Why the other options are wrong**

- A — Nothing is recovered. Personal pay arises under rule 7(7) where the OLD emoluments exceed the new, which is the opposite situation.
- B — That is the position under clause (i) alone. Clause (ii) exists precisely to stop the product being used when it falls below the first cell.
- D — Level 1 has no cell of ₹15,500 at all; its first cell is ₹18,000.

**Exam-safe point: Product below the first cell → the first cell is the pay, under clause (ii).**

> *Authority:* Rules 7(1)(A)(i) and 7(1)(A)(ii), CCS (Revised Pay) Rules, 2016

---

## Q4. [PY-004] An officer drawing ₹32,300 in Level 4 is granted his annual increment. What is his pay after it, and by how much did it rise?

*Level 4 — cell:* 8 | 9 | 10 | 11 | 12
*Pay:* ₹31,400 | ₹32,300 | ₹33,300 | ₹34,300 | ₹35,300

- (A) ₹33,269, a rise of ₹969
- (B) ₹34,300, a rise of ₹2,000
- (C) ₹34,169, being 3% of ₹33,300 added on
- (D) ₹33,300, a rise of ₹1,000 **← answer**

**Answer: (D)**

**Stepwise solution**

1. Rule 9 says the increment is as specified in the vertical cells of the Level: the officer moves down one cell in Level 4.
2. In Level 4, ₹32,300 is cell 9 and the next cell down is cell 10, ₹33,300. That is the pay after the increment.
3. The rise is ₹1,000. Note that it is NOT 3% of ₹32,300 — 3% would be ₹969. The matrix rounds each cell to the nearest ₹100, so the actual step varies from cell to cell instead of being a flat percentage.

**Why the other options are wrong**

- A — That applies 3 per cent to ₹32,300 instead of taking the next printed cell. Rule 9 moves the servant one cell, and the cell is ₹33,300.
- B — That is two cells, not one. One increment is one vertical cell.
- C — 3% of ₹32,300 is ₹969, and rule 9 does not ask for a percentage at all: it directs the officer to the next printed cell, which the matrix has already set at ₹33,300.

**Exam-safe point: Increment = next vertical cell. Read the matrix; do not compute 3%.**

> *Authority:* Rule 9 and its gazette illustration, CCS (Revised Pay) Rules, 2016

---

## Q5. [PY-005] A servant is drawing the last cell of Level 1, ₹56,900. What happens on his increment date?

*Level 1 — cell:* 38 | 39 | 40
*Pay:* ₹53,600 | ₹55,200 | ₹56,900

- (A) There is no further cell, so his pay stays at ₹56,900 **← answer**
- (B) He is granted two increments in Level 2 on promotion instead
- (C) His pay rises by 3% to ₹58,607, rounded to ₹58,600
- (D) He moves to the first cell of Level 2, ₹19,900

**Answer: (A)**

**Stepwise solution**

1. Rule 9 gives the increment by moving down the vertical cells of the Level. Level 1 has forty cells and ₹56,900 is the fortieth.
2. There is no forty-first cell, so there is nowhere for the increment to go.
3. The pay remains ₹56,900. The officer is not moved into Level 2 — promotion and MACP change the Level, an increment never does.

**Why the other options are wrong**

- B — The two-increment re-fixation belongs to the FR 22(I)(a)(1) option on promotion, not to an annual increment.
- C — There is no cell of ₹58,600 in Level 1; the Level ends at ₹56,900 and the matrix cannot be extended by arithmetic.
- D — That would be a move to a LOWER figure, and in any case an increment cannot change the Level.

**Exam-safe point: Top of the Level: the pay stands still. Only promotion or MACP changes the Level.**

> *Authority:* Rule 9, CCS (Revised Pay) Rules, 2016

---

## Q6. [PY-006] A servant is appointed on 15 March 2016. On which date does he earn his first annual increment?

- (A) 1 July 2016
- (B) 1 January 2017 **← answer**
- (C) 1 July 2017
- (D) 15 March 2017, on the anniversary of his appointment

**Answer: (B)**

**Stepwise solution**

1. Rule 10 gives two increment dates, 1 January and 1 July, and rule 10(2) decides which is yours by the half-year of appointment.
2. 15 March falls between 2 January and 1 July (both inclusive). Rule 10(2) assigns that period to 1 JANUARY.
3. So his first increment accrues on 1 January 2017, and thereafter annually on 1 January. Note the direction: the earlier half-year of appointment produces the LATER-looking date, 1 January, because the increment comes after the July date has passed.

**Why the other options are wrong**

- A — 1 July 2016 is four months after his appointment and belongs to the other half-year. The period 2 January to 1 July earns its increment on 1 January, not 1 July.
- C — That is the date for an appointment between 2 July and 1 January, which is the wrong half-year for 15 March.
- D — Anniversary increments disappeared with the sixth pay commission. Rule 10 fixes two dates in the year, not the date of joining.

**Exam-safe point: Appointed 2 January–1 July → increment on 1 January. Appointed 2 July–1 January → increment on 1 July.**

> *Authority:* Rule 10(2), CCS (Revised Pay) Rules, 2016

---

## Q7. [PY-007] A servant already in service is granted MACP in Level 6 on 10 August 2016. On which date does the financial upgradation give him his next increment?

- (A) 1 July 2016
- (B) 1 January 2017
- (C) 1 July 2017 **← answer**
- (D) 10 August 2017, one year after the MACP

**Answer: (C)**

**Stepwise solution**

1. Rule 10(2) again: the half-year of the appointment, promotion or financial upgradation decides the date.
2. 10 August falls between 2 July and 1 January (both inclusive), and that period is assigned to 1 JULY.
3. The next 1 July after 10 August 2016 is 1 July 2017, so that is the date. The increment is given in Level 6, the Level he was placed in by the MACP.

**Why the other options are wrong**

- A — That date had already passed when the MACP was granted in August 2016.
- B — 1 January is the date for the other half-year, 2 January to 1 July. August falls after that window.
- D — MACP does not create an anniversary; it only decides which of the two fixed dates applies.

**Exam-safe point: Appointed or upgraded 2 July–1 January → 1 July.**

> *Authority:* Rule 10(2), CCS (Revised Pay) Rules, 2016

---

## Q8. [PY-008] An officer drawing ₹28,700 in Level 4 is promoted to a post in Level 5. What is his pay on promotion?

*Level 5 — cell:* 1 | 2 | 3 | 4 | 5
*Pay:* ₹29,200 | ₹30,100 | ₹31,000 | ₹31,900 | ₹32,900

- (A) ₹31,000, by giving the increment in Level 5 instead of Level 4
- (B) ₹29,200, the first cell of Level 5 nearest his old pay
- (C) ₹29,600, because that is his pay after the increment
- (D) ₹30,100, at cell 2 of Level 5 **← answer**

**Answer: (D)**

**Stepwise solution**

1. Rule 13(i) works in two steps and the order is mandatory. First, give ONE increment in the Level from which he is promoted: ₹28,700 is cell 5 of Level 4, so the next cell is ₹29,600.
2. Second, place ₹29,600 in Level 5 at the cell equal to it, and if there is none, at the next higher cell. Level 5 has no ₹29,600: cell 1 is ₹29,200 and cell 2 is ₹30,100.
3. So the pay on promotion is ₹30,100, cell 2 of Level 5. The gain is ₹1,400, of which ₹900 is the increment in the old Level and ₹500 the landing on the next higher cell.

**Why the other options are wrong**

- A — Giving the increment in the new Level is the classic error. ₹28,700 raised one cell in Level 5 is ₹30,100, and then a further cell would take him to ₹31,000 — two increments for one promotion.
- B — The placement is equal-or-next-HIGHER. ₹29,200 is below ₹29,600, so it cannot be the cell.
- C — ₹29,600 is the stepping stone, not the destination. It is a Level 4 figure and he has been promoted out of Level 4.

**Exam-safe point: Increment in the OLD Level first, then equal-or-next-higher cell in the NEW Level.**

> *Authority:* Rule 13(i) and its gazette illustration, CCS (Revised Pay) Rules, 2016

---

## Q9. [PY-009] An officer drawing ₹44,900 in Level 7 is promoted to Level 8. Level 8's cells run ₹47,600, ₹49,000, ₹50,500. What is his pay on promotion?

*Level 8 — cell:* 1 | 2 | 3 | 4
*Pay:* ₹47,600 | ₹49,000 | ₹50,500 | ₹52,000

- (A) ₹47,600 — but only if his stepped figure in Level 7 is ₹46,200 **← answer**
- (B) ₹46,200, the figure after the increment
- (C) ₹49,000, the cell after ₹47,600
- (D) ₹44,900, unchanged, because the promotion is within the same Pay Band

**Answer: (A)**

**Stepwise solution**

1. Take the increment in Level 7 first. ₹44,900 is cell 1 of Level 7, so the next cell is ₹46,200.
2. Now look for ₹46,200 in Level 8. Level 8 runs ₹47,600, ₹49,000 and ₹50,500, so there is no ₹46,200 and the rule takes the next higher cell, ₹47,600.
3. The gain is ₹2,700, which is unusually large for a promotion precisely because the conversion from Level 7 to Level 8 is a big jump at the bottom of the two columns.

**Why the other options are wrong**

- B — That is a Level 7 figure. The officer is now in Level 8 and must be placed on a Level 8 cell.
- C — That would be the next higher cell after the landing cell, giving him two steps instead of one.
- D — Both Levels sit in the PB-2 band of the old structure, but Levels 7 and 8 are different Levels and promotion fixes pay in the new one.

**Exam-safe point: The increment comes in the old Level even when the new Level's first cell is far above it.**

> *Authority:* Rule 13(i), CCS (Revised Pay) Rules, 2016

---

## Q10. [PY-010] An official in Level 4 drawing ₹30,500 is granted MACP in Level 5. What is his pay, and does anything else about his post change?

*Level 5 — cell:* 1 | 2 | 3 | 4 | 5
*Pay:* ₹29,200 | ₹30,100 | ₹31,000 | ₹31,900 | ₹32,900

- (A) ₹31,000 in Level 5
- (B) ₹31,900 in Level 5, with no change of duties **← answer**
- (C) ₹32,900 in Level 5, on the footing that the upgradation also upgrades the duties
- (D) ₹30,500, unchanged until a vacancy in Level 5 arises

**Answer: (B)**

**Stepwise solution**

1. MACP is fixed exactly like a promotion under rule 13(i). First the increment in Level 4: ₹30,500 is cell 7, so ₹31,400.
2. Then place ₹31,400 in Level 5: cell 1 is ₹29,200 and cell 2 is ₹30,100, cell 3 is ₹31,000 and cell 4 is ₹31,900. There is no ₹31,400, so the next higher cell is ₹31,900.
3. His pay is ₹31,900. But MACP is a financial upgradation only: it confers no change of duties, no change of designation and no higher responsibility, which is what distinguishes it from a promotion even though the arithmetic is identical.

**Why the other options are wrong**

- A — ₹31,000 is below ₹31,400, the stepped figure, so the rule cannot place him there.
- C — The arithmetic is right and the consequence is wrong. MACP confers no higher duties; that is its defining feature.
- D — MACP needs no vacancy. That is the whole reason the scheme exists alongside promotion.

**Exam-safe point: MACP = the rule 13 arithmetic with none of the promotion's consequences.**

> *Authority:* Rule 13(i) read with the MACPS, CCS (Revised Pay) Rules, 2016

---

## Q11. [PY-011] On promotion an officer from Level 4 to Level 5 exercises the option to have his pay fixed from his next increment date. He was drawing ₹30,500 in Level 4. What happens?

*Level 5 — cell:* 2 | 3 | 4 | 5 | 6 | 7 | 8
*Pay:* ₹30,100 | ₹31,000 | ₹31,900 | ₹32,900 | ₹33,900 | ₹34,900 | ₹35,900

- (A) He is placed at ₹31,000 and stays there until his next promotion
- (B) He is placed at ₹31,900 in Level 5 at once, that being the ordinary promotion fixation under rule 13
- (C) ₹31,000 at once, re-fixed at ₹32,900 on the DNI **← answer**
- (D) He gets two increments in Level 5 on the increment date

**Answer: (C)**

**Stepwise solution**

1. Under the option he is first placed at the NEXT HIGHER cell of the promoting Level without any increment in the old Level: ₹30,500 in Level 5 58 lands at cell 3, ₹31,000. He draws that until his increment date.
2. On the increment date in the old Level he is re-fixed with TWO increments there — one for the annual increment and one for the promotion. ₹30,500 is cell 7 of Level 4, so two cells down is cell 9, ₹32,300.
3. He is then placed at the cell equal to or next higher than ₹32,300 in Level 5. Level 5 has no ₹32,300: cell 4 is ₹31,900 and cell 5 is ₹32,900. So he ends on ₹32,900, cell 5. The option beats the immediate placement of ₹31,000 by ₹1,900, which is why an officer takes it.

**Why the other options are wrong**

- A — The re-fixation is the whole point of the option. It happens on the date of his next increment in the old Level.
- B — That is what happens WITHOUT the option. Exercising the option replaces the increment-first step with the next-higher-cell placement.
- D — Both increments are given in the Level FROM WHICH he is promoted, Level 4. Only then is he placed in Level 5.

**Exam-safe point: Option: next higher cell now, two increments in the old Level on the DNI, then land in the new Level.**

> *Authority:* FR 22(I)(a)(1) as applied to rule 13, CCS (Revised Pay) Rules, 2016

---

## Q12. [PY-012] A candidate is appointed by direct recruitment to a Level 7 post on 1 September 2016. What is his pay?

*Level 7 — cell:* 1 | 2 | 3 | 4
*Pay:* ₹44,900 | ₹46,200 | ₹47,600 | ₹49,000

- (A) ₹46,200, the second cell of Level 7, because he joined mid-year
- (B) ₹1,00,000, negotiated on the strength of his last employer's pay
- (C) ₹1,15,393, being ₹44,900 × 2.57
- (D) ₹44,900, the first cell of Level 7 **← answer**

**Answer: (D)**

**Stepwise solution**

1. Rule 8 fixes the pay of a direct recruit appointed on or after 1 January 2016 at the minimum pay or the FIRST CELL of the Level.
2. The first cell of Level 7 is ₹44,900. There is no multiplication by 2.57, because a direct recruit has no existing basic pay to multiply.
3. He is also entitled to only one increment a year, and by rule 10(2) his first one falls on 1 January 2017, not on the anniversary of his joining.

**Why the other options are wrong**

- A — Joining part-way through a year does not advance the starting cell. Rule 8 fixes the first cell, and the partial year is dealt with by the date of the first increment.
- B — Personal pay arises under rule 8's proviso only for those appointed between 01.01.2016 and the notification whose existing emoluments were higher. A fresh direct recruit has no such protection.
- C — The fitment factor applies only to an existing basic pay under rule 7. A direct recruit has none; rule 8 gives him the first cell outright.

**Exam-safe point: Direct recruit on or after 01.01.2016: first cell, no fitment.**

> *Authority:* Rule 8, CCS (Revised Pay) Rules, 2016

---

## Q13. [PY-013] A person appointed to his first Government post on 10 February 2016 asks to remain on the sixth pay commission structure. What is the position?

- (A) He cannot exercise it **← answer**
- (B) He may opt for the old structure in respect of one Pay Band and Grade Pay only, that being the limit in Explanation 1
- (C) He may opt, because he had not joined when the rules were notified on 25 July 2016
- (D) He may opt for the old structure, but only until the date of his first increment in it

**Answer: (A)**

**Stepwise solution**

1. Rule 5's first proviso lets an existing servant elect to stay on the old structure until his next increment there.
2. Explanation 2 closes that door: the option is not admissible to any person appointed to a post for the first time in Government service, or by transfer from another post, on or after 1 January 2016.
3. Appointed on 10 February 2016, he is squarely inside the exclusion. He draws pay only in the revised structure, at the first cell of his Level, under rule 8.

**Why the other options are wrong**

- B — Explanation 1's one-scale limit applies to servants who HAVE the option. It cannot enlarge a facility that Explanation 2 has withheld.
- C — The dividing line is 1 January 2016, the date of effect, not 25 July 2016, the date of notification.
- D — The time limit exists for existing servants. Explanation 2 removes the option altogether from those appointed on or after 01.01.2016.

**Exam-safe point: Option exists for pre-01.01.2016 servants only, one scale, and only to the next increment.**

> *Authority:* Rule 5 and Explanations 1 and 2, CCS (Revised Pay) Rules, 2016

---

## Q14. [PY-014] A servant receives the option form but never returns it. What is his position?

- (A) His case is referred to the Central Government for interpretation
- (B) He is deemed to have elected the revised pay structure with effect from 1 January 2016 **← answer**
- (C) He is deemed to have elected the revised structure, but only from the date the three months expire
- (D) He continues on the existing structure indefinitely

**Answer: (B)**

**Stepwise solution**

1. Rule 6(1) requires the option in writing within three months of notification, with a proviso for those out of India or under suspension.
2. Rule 6(3) then supplies the default: if the intimation is not received within the time specified, the servant is DEEMED to have elected the revised pay structure with effect from 1 January 2016.
3. So failing to choose is itself a choice, and it is the choice that gives him the revised structure from the earliest date. Rule 6(4) makes whatever choice results — express or deemed — final.

**Why the other options are wrong**

- A — Rule 17 referral is for genuine questions of interpretation. Rule 6(3) answers this one in terms.
- C — The deeming is expressly with effect from 1 January 2016. The three-month period is the time for choosing, not the date from which pay is revised.
- D — Continuing on the old structure requires a positive election under rule 5. Doing nothing produces the revised structure, not the old one.

**Exam-safe point: No option in three months → deemed election of the revised structure from 01.01.2016, and it is final.**

> *Authority:* Rules 6(1), 6(3) and 6(4), CCS (Revised Pay) Rules, 2016

---

## Q15. [PY-015] What was the first cell of Level 13 in the Schedule as originally notified, and what is it today?

*As notified:* ₹118,500 | ₹122,100 | ₹125,800 | ₹129,600 | ₹133,500
*After 16.05.2017:* ₹123,100 | ₹126,800 | ₹130,600 | ₹134,500 | ₹138,500

- (A) ₹1,31,100 today, and ₹1,18,500 as notified, the column having been re-cast upward twice
- (B) ₹1,21,200, the average of the two columns, the level having been re-cast twice
- (C) ₹1,18,500, then ₹1,23,100 **← answer**
- (D) ₹1,23,100 both as notified and today

**Answer: (C)**

**Stepwise solution**

1. Part A of the Schedule to G.S.R. 721(E), notified on 25 July 2016, printed Level 13 with a first cell of ₹1,18,500, the same 2.57 index of rationalisation used for Levels 1 to 5.
2. By a Department of Expenditure resolution dated 16 May 2017 the index of rationalisation for Level 13 was raised from 2.57 to 2.67, and the whole column was re-cast. Its first cell became ₹1,23,100.
3. The gap at the first cell is ₹4,600 and it widens down the column: the twentieth cell moved from ₹2,07,900 to ₹2,15,900. No other Level was touched, so Level 13 is now the only column in the matrix carrying an IOR of 2.67 that was originally 2.57.

**Why the other options are wrong**

- A — ₹1,31,100 is the first cell of Level 13A, a different Level altogether.
- B — That reads the gazette of 2016 as the last word. The 2017 resolution re-cast the column, and questions about pay today must use ₹1,23,100.
- D — The 2016 Schedule printed ₹1,18,500. The figure moved a year later; it did not start there.

**Exam-safe point: Level 13: 1,18,500 in the 2016 Schedule; 1,23,100 from 16.05.2017. IOR 2.57 → 2.67.**

> *Authority:* Part A of the Schedule to G.S.R. 721(E) and the Department of Expenditure resolution dated 16.05.2017

---

## Q16. [PY-016] A Level 13 officer was on the fourth cell of the Level. By how much did his pay rise when the Level was re-cast on 16 May 2017?

*As notified:* ₹129,600 | ₹133,500 | ₹137,500
*After 16.05.2017:* ₹134,500 | ₹138,500 | ₹142,700

- (A) Nothing, because the revision applied only to officers appointed after 16 May 2017
- (B) ₹8,000, the same gap as at the top of the column
- (C) ₹4,600, the same as at the first cell
- (D) ₹4,900 **← answer**

**Answer: (D)**

**Stepwise solution**

1. The column as notified ran ₹1,18,500, ₹1,22,100, ₹1,25,800, ₹1,29,600, so the fourth cell was ₹1,29,600.
2. The re-cast column runs ₹1,23,100, ₹1,26,800, ₹1,30,600, ₹1,34,500, so the corresponding cell is ₹1,34,500.
3. The rise is ₹4,900. Note that it is not the flat ₹4,600 seen at the first cell: because the new column is built at 2.67 rather than 2.57, the gap widens as you move down, and at the twentieth cell it has reached ₹8,000.

**Why the other options are wrong**

- A — The re-cast column applies to the Level itself. Every officer serving in it moved to the corresponding new cell.
- B — The revision re-cast every cell of the column. An officer anywhere in Level 13 was affected from his own cell.
- C — ₹4,600 is the gap at cell 1 only. Because the two columns are built on different indices, the gap grows with every cell: ₹4,700 at cell 2, ₹4,800 at cell 3, ₹4,900 at cell 4.

**Exam-safe point: The gap widens down the column: ₹4,600 at cell 1, ₹4,900 at cell 4, ₹8,000 at cell 20.**

> *Authority:* Department of Expenditure resolution dated 16.05.2017 revising Level 13 of the Schedule

---

## Q17. [PY-017] Level 4 cell 1 is ₹25,500 and cell 2 is ₹26,300. Why is the step ₹800 rather than the ₹765 that 3% would give?

*Level 4 — cell:* 1 | 2 | 3 | 4 | 5 | 6 | 7
*Pay:* ₹25,500 | ₹26,300 | ₹27,100 | ₹27,900 | ₹28,700 | ₹29,600 | ₹30,500

- (A) Because 3% is rounded to the nearest ₹100 **← answer**
- (B) Because the level has a fixed annual increment of ₹800
- (C) Because the 3% is applied to the first cell of the Level each time
- (D) Because each cell is 3% of the one before it, rounded UP to the next ₹100

**Answer: (A)**

**Stepwise solution**

1. 3% of ₹25,500 is ₹765, which would give ₹26,265.
2. The matrix does not carry ₹26,265 or even ₹26,300 by accident: it carries the nearest multiple of ₹100, so ₹26,265 becomes ₹26,300 and the step appears as ₹800.
3. That single rounding decision is what makes all 543 cells of the matrix reproducible: apply 3% and round to the nearest ₹100 to each cell in turn, and every column regenerates exactly from its first cell, including the Level 13 column after the 2017 revision.

**Why the other options are wrong**

- B — There is no fixed increment. Level 4 steps are ₹800, ₹800, ₹800, ₹800, ₹900, ₹900 — they drift as the rounding falls differently at each cell.
- C — That would give the same step at every cell. The step changes precisely because each cell is 3% of the PREVIOUS cell.
- D — Rounding up does not reproduce the matrix. ₹18,000 plus 3% is ₹18,540; rounded up that is ₹18,600, but the matrix carries ₹18,500. Rounding to the NEAREST ₹100 gives ₹18,500 and matches every cell.

**Exam-safe point: Cell n+1 = cell n × 1.03, rounded to the nearest ₹100. That regenerates all 543 cells.**

> *Authority:* Part A of the Schedule, 7th CPC Report Table 3 and the Government's rounding practice

---

## Q18. [PY-018] Two servants both hold Grade Pay ₹5,400 on 31 December 2015, one in Pay Band 2 and one in Pay Band 3. Which Levels do they enter?

- (A) Level 9 and Level 11 respectively, one Level apart for two Pay Bands apart
- (B) Level 9 for the PB-2 holder and Level 10 for the PB-3 holder **← answer**
- (C) Both enter Level 10, because ₹5,400 is a PB-3 grade pay
- (D) Both enter Level 9, because the Grade Pay is the same

**Answer: (B)**

**Stepwise solution**

1. Rule 4 says the Level is determined by the corresponding existing Pay Band AND Grade Pay as specified in the matrix, so both halves of the old description matter.
2. In the caption row of Part A, Grade Pay ₹5,400 appears twice: against Level 9 under Pay Band 5200-20200 (PB-2) and against Level 10 under Pay Band 15600-39100 (PB-3).
3. So the PB-2 servant enters Level 9 at ₹53,100 and the PB-3 servant enters Level 10 at ₹56,100. Same grade pay, different Level, because the Pay Band is the other half of the key.

**Why the other options are wrong**

- A — The mapping is fixed by the caption, not by counting bands. PB-2 Grade Pay ₹5,400 is Level 9 and PB-3 Grade Pay ₹5,400 is Level 10.
- C — It is a PB-3 grade pay and also a PB-2 grade pay. The matrix caption carries both mappings.
- D — Grade Pay alone is not the key. ₹5,400 maps to Level 9 in PB-2 and Level 10 in PB-3.

**Exam-safe point: Level = Pay Band + Grade Pay. ₹5,400 in PB-2 is Level 9; ₹5,400 in PB-3 is Level 10.**

> *Authority:* Rule 4 and the caption row of Part A of the Schedule

---

## Q19. [PY-019] A medical officer has existing basic pay of ₹21,000 and draws Non Practicing Allowance at 25 per cent, with dearness allowance at 125 per cent on the NPA as on 1 January 2006. What is his pay in the revised structure?

*Level 10 — cell:* 1 | 2 | 3 | 4 | 5 | 6
*Pay:* ₹56,100 | ₹57,800 | ₹59,500 | ₹61,300 | ₹63,100 | ₹65,000

- (A) ₹66,550, at cell 6 of Level 10
- (B) ₹54,300, on the product of ₹53,970 alone
- (C) ₹61,300, at cell 4 of Level 10 **← answer**
- (D) ₹60,533, because the product of the multiplication is the revised pay

**Answer: (C)**

**Stepwise solution**

1. First take the NPA: 25 per cent of ₹21,000 = ₹5,250.
2. Now apply the fitment factor: ₹21,000 × 2.57 = ₹53,970. There is no fraction here, so nothing to round.
3. Next the extra element that clause (B) adds: dearness allowance on the pre-revised NPA. 125 per cent of ₹5,250 = ₹6,562.50, rounded UP to ₹6,563.
4. Add it: ₹53,970 + ₹6,563 = ₹60,533.
5. Locate ₹60,533 in Level 10. Cell 3 is ₹59,500 and cell 4 is ₹61,300. There is no cell of ₹60,533, so the rule takes the next higher cell — ₹61,300 at cell 4.
6. Rule 7(1)(B)(ii) then allows the pre-revised NPA of ₹5,250 to be added on top, so the officer draws ₹66,550 in all until the revised rates of NPA are settled. That second figure is not part of his basic pay.

**Why the other options are wrong**

- A — That is pay plus NPA. ₹66,550 is not a cell of Level 10, and the NPA sits outside the matrix — it is added on top of the pay, not located in the Level.
- B — Clause (B) adds the dearness allowance on the NPA to the product before the cell is found.
- D — Rule 7(1)(A) locates the figure in the matrix; ₹60,533 is not a printed cell.

**Exam-safe point: NPA: 21,000 × 2.57 = 53,970; plus 125% of 5,250 = 6,563; total 60,533 → ₹61,300 at cell 4 of Level 10.**

> *Authority:* Rule 7(1)(B) and its illustration, CCS (Revised Pay) Rules, 2016

---

## Q20. [PY-020] An officer in Level 11 was drawing existing basic pay of ₹44,900 on 1 January 2016. What is his revised pay?

*Level 11 — cell:* 16 | 17 | 18 | 19 | 20 | 21 | 22
*Pay:* ₹105,600 | ₹108,800 | ₹112,100 | ₹115,500 | ₹119,000 | ₹122,600 | ₹126,300

- (A) ₹1,12,100, at cell 18 of Level 11
- (B) ₹1,15,400, rounding the product to the nearest ₹100 and then taking that cell
- (C) ₹1,15,393, the exact product
- (D) ₹1,15,500, at cell 19 of Level 11 **← answer**

**Answer: (D)**

**Stepwise solution**

1. Multiply: ₹44,900 × 2.57 = ₹1,15,393.
2. There is no fraction to round away, so the figure to locate is ₹1,15,393.
3. Look for it in Level 11. Cell 18 is ₹1,12,100 and cell 19 is ₹1,15,500. There is no cell of ₹1,15,393.
4. The rule takes the next higher cell, so the pay is fixed at ₹1,15,500 on cell 19.
5. The servant gains ₹107 over the exact product. That is the working of the rule, not an error: the excess is never recovered and never carried forward as a debt.

**Why the other options are wrong**

- A — That is the cell below the product. Rule 7(1)(A)(i) goes up, never down.
- B — Rounding the product to ₹100 is not part of the rule; rounding the CELLS to ₹100 was done when the matrix was built. The figure to locate is ₹1,15,393, and it lands on ₹1,15,500.
- C — The product is a step, not a pay. It has to be located at a printed cell, and only a cell can be drawn.

**Exam-safe point: Even at the top of the matrix the method is the same: multiply, round to the rupee, take the equal or next higher cell.**

> *Authority:* Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016

---

## Q21. [PY-021] An official drawing ₹35,400 in Level 6 is granted MACP in Level 7. Level 7 opens at ₹44,900. What is his pay after the upgradation?

*Level 7 — cell:* 1 | 2 | 3
*Pay:* ₹44,900 | ₹46,200 | ₹47,600

- (A) ₹44,900, at cell 1 of Level 7 **← answer**
- (B) ₹45,800, by adding the forfeited increment to the first cell of Level 7
- (C) ₹47,600, the second cell, so that he is seen to have gained a step
- (D) ₹36,500, the stepped figure, with the difference paid as personal pay

**Answer: (A)**

**Stepwise solution**

1. Rule 13(i) first gives one increment in the Level he is in: ₹35,400 is cell 1 of Level 6, so the step is to ₹36,500 on cell 2.
2. Now locate ₹36,500 in Level 7. Level 7 opens at ₹44,900, which is already higher than ₹36,500.
3. So there is no cell equal to or above ₹36,500 other than the first — the pay is fixed at ₹44,900 on cell 1.
4. The gain is ₹9,500, and almost all of it is the distance between the two Levels rather than the increment.

**Why the other options are wrong**

- B — The increment has been given — in Level 6, as the rule requires. Nothing is forfeited.
- C — The rule takes the equal or next higher cell, and the first cell is already higher than the stepped figure. There is no reason to skip it.
- D — Personal pay protects an excess of old over new emoluments. Here the new figure is far higher, so nothing is protected and nothing is added.

**Exam-safe point: When the new Level's first cell is above the stepped figure, the first cell IS the equal-or-next-higher cell.**

> *Authority:* Rule 13(i) and the MACP scheme, CCS (Revised Pay) Rules, 2016

---

## Q22. [PY-022] On promotion from Level 4 to Level 5 an officer drawing ₹30,500 opts to have his pay fixed from the date of his next increment. He gets two increments in Level 4 from ₹30,500. What does he draw in the meantime, and what is he fixed at?

*Level 5 — cell:* 2 | 3 | 4 | 5 | 6 | 7 | 8
*Pay:* ₹30,100 | ₹31,000 | ₹31,900 | ₹32,900 | ₹33,900 | ₹34,900 | ₹35,900

- (A) ₹31,900 meanwhile; ₹32,900 on the increment date
- (B) ₹31,000 meanwhile; ₹32,900 on the increment date **← answer**
- (C) ₹31,400 meanwhile, and re-fixed at ₹32,900 on the increment date
- (D) ₹33,300 on the increment date, two increments above ₹31,000

**Answer: (B)**

**Stepwise solution**

1. Under the option he continues on the old Level until his next increment date, and is placed at the cell above his present pay in the NEW Level for that period: ₹30,500 steps to ₹31,000 on cell 3 of Level 5.
2. On the increment date he is given TWO increments in the Level he came from, Level 4: ₹30,500 (cell 7) → ₹31,400 (cell 8) → ₹32,300 (cell 9).
3. Then ₹32,300 is located in Level 5. It is not a cell there — cell 4 is ₹31,900 and cell 5 is ₹32,900 — so the next higher cell is taken.
4. He is re-fixed at ₹32,900 on cell 5. The interim ₹31,000 is replaced, not added to.

**Why the other options are wrong**

- A — The interim placement is the cell above his present pay, which is ₹31,000 on cell 3. ₹31,900 is two cells up.
- C — The option defers the fixation; it does not cancel it. On the increment date the pay is re-fixed with two increments.
- D — The two increments are taken in Level 4, the Level he is promoted FROM. Taking them in Level 5 pays them at the higher Level's rates and overstates the figure by ₹400.

**Exam-safe point: The two increments are ALWAYS in the old Level. 30,500 → 31,400 → 32,300, then re-fixed at ₹32,900.**

> *Authority:* FR 22(I)(a)(1), read with rule 13(i), CCS (Revised Pay) Rules, 2016

---

## Q23. [PY-023] The fitment factor of 2.57 is applied to existing basic pay. Roughly what rise does it represent for a servant, before the move to the equal or next higher cell?

- (A) About 3 per cent
- (B) About 57 per cent
- (C) About 157 per cent **← answer**
- (D) 257 per cent, since the factor itself is 2.57

**Answer: (C)**

**Stepwise solution**

1. The factor is what the old basic pay is multiplied by, so the new figure is 2.57 times the old.
2. The RISE is the new figure less the old: 2.57 − 1 = 1.57, which is 157 per cent of the old basic pay.
3. So a servant on ₹12,560 who is multiplied by 2.57 moves to ₹32,279 — a rise of ₹19,719, which is 157 per cent of ₹12,560.
4. This rise is what absorbs the 6th CPC dearness allowance and the grade pay rationalisation. It is not a pay rise in real terms; it is a conversion.

**Why the other options are wrong**

- A — Three per cent is the annual increment built into the matrix, not the conversion factor.
- B — That would be a factor of 1.57. The factor is 2.57, and the rise over the old pay is 157 per cent.
- D — That is the factor expressed as a percentage of the old pay, not the rise. The rise is 2.57 − 1 = 1.57.

**Exam-safe point: Factor 2.57 = an increase of 157 per cent. The difference between the two numbers is one.**

> *Authority:* Rule 7(1)(A)(i), CCS (Revised Pay) Rules, 2016

---
