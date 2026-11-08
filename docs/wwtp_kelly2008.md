# Sewage treatment plants and Kelly et al. (2008): Site 2 and the other study sites

Compiled 2026-11-08. Reviewer comment: "A sewage treatment plant and septic systems lie upstream (according to the same study site evaluated in Kelly et al., 2008)".

## 1. What Kelly et al. 2008 says

Kelly, Lovett, Weathers, Findlay, Strayer, Burns & Likens (2008), Environ. Sci. Technol. 42(2):410-415, doi 10.1021/es071391l.
Read from the Cary Institute reprint PDF (6 pages, article pp. 410-415): https://www.caryinstitute.org/sites/default/files/public/reprints/Kelly_et_al_EST_2008.pdf
Text extracted with pypdf; quotes are from that extraction (ligatures normalised).

**Watershed, site, plant, septic (p. 410, Materials and Methods):**
- "The study site is the East Branch of Wappinger Creek and its watershed in Dutchess County, NY. The watershed area is 6243 ha, and the land use is 91% forested or open field and 9% residential and commercial. There are 136 km of road surface in the watershed (3.9 km of them are dirt roads) and 6 ha of parking surface."
- "The village of Millbrook with a 2005 population of 1559 is the only municipality within this watershed. The Millbrook sewage treatment plant is approximately 3 km upstream from the sampling site for this project. Total population of the watershed in 2005 was 2539. Approximately 44% of the people in the watershed are served by private wells and septic systems, and the remainder use the Millbrook village public water supply and sewage system."
- "Stream samples were collected at the end of every month at the Cary Arboretum, Institute of Ecosystem Studies (IES), in Millbrook, NY (N41.786 W073.741)." (p. 410)

**How the sewage load was estimated (p. 411):**
- "We calculated sewage (septic and sewage treatment plant) input to the watershed using an estimate of 3.3 kg chloride per person per year by excretion, 9.1 kg chloride per person per year from other household wastes, 0.73 kg per person per year from chlorination at the sewage treatment plant (6), and 4.95 kg sodium per person per year from NaHCO3 used at the Millbrook sewage treatment facility to neutralize pH."
- The paper gives no plant discharge volume, no permit number and no plant coordinates; the plant load is a per-capita estimate, not a measured effluent flux. The plant and septic loads are combined into one "sewage" term.

**Source shares (p. 412, Results, Input; Table 1 same page):**
- "municipal roadway anti-icing salt contributed 83% and parking area anti-icing salt contributed 8% ... Thus, 91% of the sodium chloride input to the watershed was from salt used for anti-icing. Sewage contributed 4% and water softeners contributed 3% of the total sodium chloride to the watershed. Only 2% of sodium and chloride was from atmospheric deposition and rock weathering. Thus 98% ... was anthropogenic."
- "Input of sodium chloride from sewage and water softeners increased during the study (86 952 kg in 1986 to 105 006 kg in 2005), but this increase only accounted for about 1% of the increase in export over the same period (878 781 kg in 1986 to 2 283 053 kg in 2005)." (p. 412)
- Table 1 sewage: 52 414 kg/yr (4%) (p. 412).
- Discussion (p. 413): "these increases [sewage effluent and water softener] were far too small to explain the increase in sodium and chloride export. Instead, we attribute the increase to a storage effect of long-term road salt use and subsurface build-up of salt."

**Confirmation of the earlier note:** all numbers in the note are confirmed (3 km, 44%, 83/8/4/3 %, wet deposition 1%, rock weathering 1%; the earlier note's "Table 1" shares sum with dry deposition <1%). Details to keep straight:
- The paper's "3 km" is the plant-to-Cary-Arboretum distance as stated by the authors. It is not stated whether this is straight-line or along the channel. Measured here (below): about 3.6 km straight-line from the ECHO plant location to N41.786 W073.741, and about 5.7 km along the NHD channel (see section 4). So "approximately 3 km" is closer to a straight-line figure.
- The 83% is the municipal roadway share only; total deicing salt is 91%.
- "Sewage 4%" combines septic and the plant. The paper does not split them.
- The plant is described only as "the Millbrook sewage treatment plant"; the paper does not mention any other sewage plant in the East Branch watershed ("the only municipality").

## 2. Facilities found (official data)

Sources, both queried 2026-11-08:
- EPA ECHO web service (CWA facilities, Dutchess County individual NPDES permits, then each facility's detailed facility report): https://echodata.epa.gov/echo/cwa_rest_services.get_facilities?output=JSON&p_st=NY&p_co=Dutchess&p_ptype=NPD and https://echodata.epa.gov/echo/dfr_rest_services.get_dfr?output=JSON&p_id=NY0025429 (and the other permit IDs).
- NYS open data "Municipal/Industrial Wastewater Treatment Plants" (NYSDEC SPDES-derived): https://data.ny.gov/resource/rsuw-xxks.json and https://data.ny.gov/resource/2v6p-juki.json

Limits of the coordinates: ECHO gives facility locations (for Millbrook "Facility Center/Centroid", collected by "Interpolation-Map", scale 1:24,000), not surveyed outfall points. NYS open data gives coordinates rounded to 0.01 degree (about 1 km), which is too coarse to use. No outfall-level coordinates were found in either source. I did not open the NYSDEC SPDES permit PDF or the NYSDEC Environmental Resource Mapper; those might give outfall positions. The DMR-based outfall coordinates in ICIS were not retrieved.

Flows: ECHO lists design flow 0.37 MGD and "actual average flow" 0.17 MGD for the Millbrook STP; the NYS open data lists average design hydraulic flow 0.25 MGD for the same permit. These disagree and I could not tell which is current (ECHO permit status: Effective, non-major individual permit, expires 12/31/2030). ECHO's detailed report also lists an open compliance-schedule event for the plant (due 04/30/2025, "Schedule Event unachieved and not reported", case 02-2025-3002); not relevant to the study dates.

Receiving water per ECHO (ICIS "water body names"): Millbrook STP, "WAPPINGER CK E BR".

Network placement was done on the NHD flowline network used by `src/rev_figures.py` (flowlines named Wappinger Creek or East Branch Wappinger Creek, ends snapped at 25 m, rooted at the southernmost node, vertices every 10 m; the geometry script is in the session scratchpad only, not in `src/`). Facility points were snapped to the nearest flowline; "snap" is the offset. Site first point = first row in field order (Site 3: first row of the 19 Oct transect, the upstream-most start). A facility is upstream of a point if the point lies on the facility's downstream path.

| Facility | Permit | Lat, lon (ECHO) | Receiving water (ECHO) | Design flow (MGD) | Snap to channel | Upstream of Site 1? | Upstream of Site 2? | Upstream of Site 3? |
|---|---|---|---|---|---|---|---|---|
| Millbrook STP (municipal) | NY0025429 | 41.7881, -73.6975 | East Branch Wappinger Creek | 0.37 ECHO / 0.25 NYS (avg actual 0.17) | 55 m | Yes; 15.3 km along channel to first point (7.2 km straight) | Yes; 25.3 km to first point (12.2 km straight), 33.6 km to last point | Yes; 2.4 km along channel to first point (1.75 km straight); 2.1 km to the nearest start of the 26 Oct upper transect |
| NYSP Troop K HQ (state police) | NY0099279 | 41.7835, -73.7540 | East Branch Wappinger Creek tributary | not listed | 581 m (tributary not in network) | Yes by drainage (8.6 km along channel from snap point) | Yes (18.6 km) | Not on the channel path: lies downstream of Site 3's survey (snaps below it); 0.8 km straight from the nearest Site 3 point |
| Stratford Farms STP (private) | NY0218944 | 41.7282, -73.8403 | Wappinger Creek | not listed | 228 m | No (downstream of Site 1) | Inside Site 2 zone 2-1: about at survey row 4 (0.24 km straight) | No |
| Ennis Mobile Home Park WWTP (private) | NY0218952 | 41.7331, -73.8396 | Wappinger Creek | not listed | 285 m | No | Inside Site 2 zone 2-1: between rows 3 and 4 (0.37 km straight) | No |
| Valley Dale STP (municipal) | NY0077593 | 41.7262, -73.8154 | Wappinger Creek tributary | 0.038 | 1766 m (tributary) | No | Enters from a tributary; location about 1.8 km from Site 2 row 4; position along Site 2 not resolvable from the facility point | No |
| Titusville WWTP (Titusville/Manchester) | NY0264989 | 41.6858, -73.8672 | Wappinger Creek | 0.5 | 61 m | No | No: snaps about 0.5 km downstream of Site 2's last point (0.47 km straight) | No |

Not sewage but listed for completeness: Pleasant Valley Quarry (NY0006173, 41.7710, -73.8127, receiving "Wappinger Ck Tr", industrial, 0.281 MGD): upstream of Site 2 (4.3 km along channel to first point by facility snap, 0.7 km snap uncertainty), not upstream of Sites 1 or 3.

Other Dutchess individual-permit wastewater facilities in the search (Greenfields SD#8, Brookside Meadows, Enclave at Hyde Park, Pinebrook Estates, Midpoint Park SD, Wildwood SD, Noxon Knolls SD, etc.) discharge to other streams (Fall Kill, Great Spring Creek, Maritje Kill, Fishkill Creek) or to Wappinger Creek tributaries well south of Site 2; none discharge above the three sites. Several of those south-of-Site-2 plants are listed as "WAPPINGER CK TR" (Midpoint, Wildwood, Noxon Knolls, old Titusville SD) and are downstream. Facilities with only general stormwater permits were not examined. A facility that is on general rather than individual permit, or a pre-2018 closed plant, would not appear in this search.

## 3. Which branch each site is on

On the NHD network:
- Site 3 is on the East Branch (all points snap to East Branch Wappinger Creek; max snap 61 m).
- Site 1 is on the main stem (Wappinger Creek), not the East Branch.
- Site 2 is on the main stem (Wappinger Creek).
- The East Branch joins the main stem at about 41.814, -73.758 (NHD), which is about 3.2 km (along channel) above Site 1's first point; so the Millbrook STP effluent reaches Sites 1 and 2 as part of the combined flow after the confluence, diluted by the main-stem flow.

## 4. Kelly et al. long-term site versus Site 3

- Kelly 2008 coordinates N41.786 W073.741 lie 333 m from the nearest Site 3 survey point (26 Oct lower transect, row 10, zone 3-4, lat 41.78323, lon -73.74254). They are 316 m off the NHD East Branch line (coordinates are given to three decimals, about 100 m, so this is a modest mismatch). So the Kelly 2008 site is at the downstream end of Site 3, in or next to zone 3-4.
- The chloride-transect point flagged "location of long-term Cl monitoring, Kelly et al., 2019 (Fig. 1)" (`load_chloride()`, lat 41.78825, lon -73.73201) is 7 m from Site 3 survey point row 19 of the 19 Oct transect (zone 3-3); it is 788 m from the Kelly 2008 coordinates. The note in the chloride file cites Kelly et al. 2019 (the Cary Institute road-salt report), not Kelly 2008. The two flagged positions differ by 0.8 km, so the sampling location as described in 2008 and 2019 may not be identical, or the 2008 coordinates are approximate; I did not check the 2019 report's Fig. 1.
- Plant to those points: Millbrook STP is upstream of both. To the flagged Cl monitoring point: 2.9 km straight, 4.6 km along channel. To the Kelly 2008 coordinates: 3.6 km straight, 5.7 km along channel.
- Plant to Site 3 zone boundaries (along channel from the plant location): zone 3-1 spans 2.1 to 2.8 km, 3-2 spans 2.9 to 3.3 km, 3-3 spans 3.4 to 5.3 km, 3-4 spans 5.5 to 6.0 km. All Site 3 zones are downstream of the plant.

## 5. Implications for the manuscript

Facts only:
1. The reviewer is right that a municipal plant lies upstream of Site 3: the Millbrook STP (NY0025429, East Branch, design flow 0.25 to 0.37 MGD depending on source) is 1.75 km straight-line and about 2.4 km along the channel above the first Site 3 survey point. It is also upstream, via the main stem, of Sites 1 and 2 (15 and 25 km along channel, after the East Branch confluence). Kelly et al. state it is the only municipality in the East Branch watershed.
2. A continuous point source above the whole survey raises the baseline specific conductance (and chloride) of the downstream reach. By itself it would not create a step at a mid-reach zone boundary, because all zones of Site 3 are downstream of it. The contrasts in Table 1 compare zones within a site, so the upstream plant contribution is common to both sides of each contrast, to first order. This is an argument by position only; no effluent concentration data were examined.
3. Kelly et al. attribute 4% of the East Branch sodium chloride input to sewage (plant plus septic combined) and 3% to water softeners, versus 83% (91% with parking-area salt) to deicing salt; they estimate the plant load from per-capita figures, not from measured effluent. Septic systems were about 44% of residents watershed-wide; the paper does not locate septic systems within the study reaches. The manuscript can cite those figures but should not claim that septic contributions were quantified along the surveyed reaches.
4. Site 2 is a separate case: two small private sewage plants listed in ECHO as discharging to Wappinger Creek (Stratford Farms STP NY0218944 and Ennis Mobile Home Park WWTP NY0218952) have facility locations within about 250 to 400 m of Site 2's survey points in zone 2-1, and Valley Dale STP (NY0077593, 0.038 MGD) discharges to a tributary about 2 km away. The Titusville WWTP (0.5 MGD) is just downstream of Site 2's last point. If either private plant discharges into zone 2-1, it could contribute to the zone 2-1 baseline; whether it does depends on the real outfall locations, which this search did not obtain. I did not find any sewage plant at the Site 2 zone 2-1/2-2 boundary (survey rows 10 and 11); the nearest facility points are 1 km or more from that boundary along the channel. Contrast statistics for Site 2 should be reported with that caveat; I did not examine Site 2's conductance profile for effects at the plant positions.
5. Wording should avoid "only road salt": the defensible statement is that deicing salt is the dominant basin-wide source (Kelly et al.: 91%), while sewage and softeners are minor basin-wide but locally present upstream and, for Site 2, possibly within the reach.
6. Before final submission, outfall coordinates for NY0025429, NY0218944 and NY0218952 should be taken from the NYSDEC SPDES permit or Environmental Resource Mapper, and Kelly 2008's 3 km (distance type unspecified) should not be restated as an along-channel distance.
