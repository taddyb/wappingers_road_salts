# Instrument specifications and uncertainty notes

Compiled 2026-11-08 from manufacturer pages and PDFs actually opened. Items not found are marked NOT FOUND. Derived numbers are my arithmetic, not manufacturer statements.

## 1. Orion 013010MD conductivity cell

Sources:
- Product page: https://www.thermofisher.com/order/catalog/product/013010MD
- Orion Conductivity Cells User Guide 254782-001 Rev B: https://documents.thermofisher.com/TFS-Assets/LPD/manuals/254782-001_B.pdf
- Orion Conductivity Probes brochure (Thermo): https://documents.thermofisher.com/TFS-Assets/LPD/brochures/orion-conductivity-probes-brochure.pdf

| Item | Stated | Source |
|---|---|---|
| Type | "4-Electrode Conductivity Cell, Waterproof 8-Din Connector"; epoxy/graphite DuraProbe, 3 m cable ("013010MD 4-Cell Rugged DuraProbe, 3 m") | product page; user guide p. 6-7 ordering table |
| Cell constant | "nominal cell constant of 0.475 cm-1" | user guide p. 1 |
| Range | "Measurement range is 1 uS/cm to 200 mS/cm." | user guide p. 1 |
| Temperature sensor | "built-in ATC temperature sensor"; brochure: probes "can withstand temperatures of 0 to 90 C" | product page; brochure |
| Cell accuracy | NOT FOUND. Neither the product page, the user guide, nor the brochure gives a numeric accuracy for the cell. The user guide says only "Thermo Scientific Orion DuraProbe cells are durable and extremely accurate under a wide range of conditions." The ATC sensor accuracy is also not stated for the cell. | all three |
| Compatible meters | "Thermo Scientific benchtop meter such as the Star A112, A212, A215, or Versa Star Pro, or portable meter such as Star A122, A222, A322, A325, or A329." Also: the 013010MD "ha[s] a connector that is compatible with the Star Series conductivity meters." | user guide p. 1 |

Calibration caveat, user guide p. 2: "Calibration is essential since the cell constant can vary as much as 10% from the nominal cell constant and the actual cell constant may change over time." Auto Cal sets the actual cell constant against a conductivity standard.

Where accuracy is specified: for the meter (and the meter+cell conductivity channel as quoted on meter pages), not for the cell as a standalone item. Thermo gives no separate system accuracy statement that I found.

## 2. Meter accuracy (meter body unknown)

Sources (Thermo product pages, spec sections):
- A222: https://thermofisher.com/order/catalog/product/STARA2220
- A322: https://www.thermofisher.com/order/catalog/product/STARA3220
- A325: https://www.thermofisher.com/order/catalog/product/STARA3250
- A212 benchtop: spec text confirmed via product listings and the A212 guide at https://documents.thermofisher.com/TFS-Assets/LED/Product-Guides/IS-68X576502-Orion-A212BT.pdf (this guide covers settings, not the accuracy table). The A212 page (STARA2120) is "not orderable at the moment" and had no spec table.

Quoted (identical wording on A222, A322, A325 pages):
- Conductivity accuracy: "0.5% of reading +/-1 digit > 3 uS; 0.5% of reading +/-0.01 uS <= 3 uS"
- Conductivity resolution: "0.001 uS minimum, auto ranging up to 4 significant digits"
- Conductivity range: "0.001 uS/cm to 3000 mS/cm"
- Temperature accuracy: "+/-0.1 C"; temperature range "-5 C to +105 C"; temperature resolution 0.1 C (A322 page)
- Temperature compensation: A322/A325: "Linear, nLFn (non-linear ultra pure water), nLFu (non-linear ultra pure degassed water), EP (off with warning) or off"; A222: "Linear, nLFn (non-linear ultra pure water) or off". Reference temperature selectable "5, 10, 15, 20, or 25 C" (A322 page).
- Repeatability: not listed on the A322 spec section. NOT FOUND for any of these meters.
- Default linear coefficient: not listed on the product pages. NOT FOUND in the official A2xx/A3xx documents I could open.

Range across compatible current meters (A222, A322, A325; A212 listing text matches): there is no range. All state the same +/-0.5% of reading +/-1 digit and +/-0.1 C. The older A122/A112/A329 and Versa Star Pro pages were not opened; do not assume they match.

Legacy-manual note on linear coefficient (NOT an official Thermo-hosted file; third-party hosting of the "Orion Star and Star Plus Series" user guide, a different series and may differ for A2xx/A3xx): https://www.manualslib.fr/manual/339495/Thermo-Scientific-Orion-Star.html?page=73
- "The closer the sample temperature is to the selected reference temperature, the more accurate the conductivity measurement will be, especially if the temperature compensation coefficient is estimated or inaccurate."
- "The meter has a default temperature coefficient of 2.1 percent change in conductivity per C, which is representative of many aqueous samples."
- The page also contains a coefficient table (ultra-pure water, NaCl, sugar syrup); I could not reliably map values to solutions, so not quoted.

Thermo smart note (official; no numbers): https://documents.thermofisher.com/TFS-Assets/LSG/Specification-Sheets/SN-10MISTAKES-E%20RevA-WEB.pdf
- "Conductivity measurements are strongly affected by the temperature of the sample."
- "Taking a conductivity reading before achieving temperature equilibrium. Conductivity is temperature-dependent, so time must be allowed for the conductivity sensor to equilibrate to the same temperature as the sample."
- "Tighter accuracy can be achieved by calibrating at 100 uS/cm or above."

## 3. Temperature-compensation uncertainty

No Thermo document I opened states a numeric error for linear compensation of natural waters, nor a numeric error as a function of distance from 25 C. The only statement is the qualitative one above (error grows with distance from reference temperature if the coefficient is inaccurate). I did not find a statement that 2.1 %/C is wrong for natural waters either; the legacy manual calls it "representative of many aqueous samples." Whether the survey meter used 2.1 or another value is unknown (default on the unknown meter not verified).

Illustrative arithmetic only (mine, not Thermo's): compensating from 8-16 C to 25 C spans 9-17 C. If the true coefficient differs from the one set by delta %/C, the compensated value is off by about delta x (25 - T) percent. For delta = 0.1 %/C and T = 10 C, that is about 1.5%, i.e. about 4.6 uS/cm at 310 uS/cm. This is a systematic (same-direction) error for readings at similar temperature, so it largely cancels in a difference between two zones measured at similar water temperature; the residual in the difference is about delta x |T1 - T2| x SC (for example 0.1 x 1 C x 310 uS/cm = 0.3 uS/cm). The temperature sensor itself (+/-0.1 C) adds, at 2.1 %/C, about 0.2% (roughly 0.65 uS/cm at 310) of compensated reading if the +/-0.1 C applies to the ATC probe in the cell.

## 4. Implied absolute uncertainty

Stated accuracy: +/-0.5% of reading +/-1 digit (reading > 3 uS). Resolution 4 significant digits, so for readings of 100-999 uS/cm the display step is 0.1 uS/cm (1 digit = 0.1 uS/cm, derived).

| Reading | 0.5% of reading | +/- 1 digit | Total (linear sum) |
|---|---|---|---|
| 310 uS/cm (Contrast B, Site 2) | 1.55 | 0.1 | about +/-1.65 uS/cm |
| 360 uS/cm (Site 3) | 1.80 | 0.1 | about +/-1.9 uS/cm |

Add about 0.6-0.7 uS/cm if the +/-0.1 C temperature sensor is propagated through 2.1 %/C (derived above); the Thermo spec is for the meter and is not stated to include temperature compensation error.

Interpretation for within-day differences (reasoning, not a manufacturer statement): the stated accuracy is a bound on total error including a systematic part (cell constant/calibration offset and gain, meter electronics). A calibration offset or gain error common to all readings taken on the same day with the same cell/meter shifts every reading by the same amount (or the same percentage), so it largely cancels in a within-day difference between two zones (a pure gain error of 0.5% changes a 4 uS/cm difference by only about 0.02 uS/cm). Random error (repeatability, probe positioning, incomplete temperature equilibrium, real short-term variation in the stream) does not cancel; it adds in quadrature in a difference. Thermo does not publish a repeatability figure for these meters or the cell in the documents I opened (NOT FOUND), so the random component cannot be quoted. The +/-1.65-1.9 uS/cm figure should therefore be read as a conservative upper bound on the absolute level, and the uncertainty of a within-day difference is expected to be smaller but is not quantified by the manufacturer. The 1.6-4.3 uS/cm zone differences are comparable to the absolute-accuracy bound, so the argument for their significance has to rest on the replicate/statistical spread of the survey readings, not on the instrument spec. A way to verify: report the within-zone standard deviation of repeated readings.

## 5. 2020 chloride transect: YSI multi-probe (model unknown)

The model is unknown, so the following is typical-range information from recent YSI literature only.

Sources:
- ProDSS specification sheet W83-04 (Sept 2016): https://res.cloudinary.com/iwh/image/upload/q_auto,g_center/assets/1/26/YSI_ProDSS_Datasheet.pdf
- ProDSS specification sheet W83-03 (July 2015): https://pentairaes.com/media/docs/YSI-ProDSS-W83-03-0715-Spec-Sheet.pdf
- ProDSS catalog: https://www.ysi.com/File%20Library/Documents/Brochures%20and%20Catalogs/YSI-ProDSS-Catalog.pdf
- ProDSS User Manual 626973 Rev B: https://pentairaes.com/media/docs/YSI-ProDSS-110714-Rev-B-626973-User-Manual.pdf
- TruLine ISE spec sheet W74 1014: https://www.ysi.com/File%20Library/Documents/Specification%20Sheets/YSI-ISE-Electrodes-W74-1014-spec-sheet.pdf
- TruLine chloride ISE manual: https://www.ysi.com/File%20Library/Documents/Manuals/Chloride-ISE-Manual-YSI-AUG2014C.PDF

Quotes:
- ProDSS spec sheets W83-03 and W83-04 (identical row): "Chloride** 0 to 18000 mg/L Cl +/-15% of reading or 5 mg/L, whichever is greater 0.01 mg/L Cl". Footnote: "ISEs for freshwater only; 20 meter maximum depth". Calibration "1, 2, or 3 point".
- ProDSS Catalog: "Chloride ISE (mg/L-Cl, mV) 0 to 1000 mg/L-Cl- 0.01 mg/L +/-15% of reading or 5 mg/L-Cl-, whichever is greater 1-, 2-, or 3-point (user-selectable)". Note the range differs between YSI documents (1000 vs 18000 mg/L); accuracy statement is identical.
- ProDSS manual (p. 44): "A 2-point calibration without chilling a third calibration solution is extremely accurate and is the preferred method. However, if there is a large temperature variation during sampling, a chilled third calibration point is recommended." Warns the sensor module working life is "4 to 8 months."
- Interferences: the ProDSS spec sheets and ProDSS manual text I extracted contain no interference list (NOT FOUND for ProDSS). For YSI's TruLine lab chloride ISE (a different product, same solid-state chloride technology, but not the ProDSS sensor): "Interferences: CN-, Br-, I-, OH-, S2-, NH3" (manual) and the spec-sheet row "Chloride (Cl-) 400393 ... 1.8 to 35,500 mg/L ... 54 to 59 mV/decade ... pH 2 to 12 ... CN-, Br-, I-, OH-, S2-, NH3". Treat as indicative only.
- EXO and 6-series chloride sensors, ProPlus chloride: NOT opened/read; no values reported.

Implied uncertainty at typical stream chloride (illustrative arithmetic): the "greater of 15% or 5 mg/L" rule gives +/-5 mg/L below 33 mg/L and +/-15% above; for example, +/-30 mg/L at 200 mg/L.

## Suggested Methods text

"Specific conductance was measured with a Thermo Scientific Orion 013010MD DuraProbe four-electrode graphite conductivity cell (nominal cell constant 0.475 cm-1; stated range 1 uS/cm to 200 mS/cm) with built-in temperature sensor, connected to an Orion Star-series conductivity meter, calibrated against conductivity standard following manufacturer procedures, with readings compensated to 25 C. For current Orion Star A222, A322 and A325 meters, the manufacturer states a conductivity accuracy of 0.5% of reading plus or minus one digit and a temperature accuracy of +/-0.1 C; the corresponding uncertainty is about +/-1.7 uS/cm at 310 uS/cm and +/-1.9 uS/cm at 360 uS/cm. Manufacturer documentation does not report a separate accuracy for the cell or a repeatability figure, and a calibration offset common to all readings in a day cancels in within-day upstream-downstream differences, whereas random error does not. Chloride in 2020 was measured with a YSI multiparameter sonde chloride ion-selective electrode; for current YSI ProDSS chloride sensors the stated accuracy is the greater of +/-15% of reading or 5 mg/L."

(Edit the meter model and the chloride sentence once the author confirms the actual instruments; do not state the A2xx/A3xx accuracy unless the meter is one of those models.)
