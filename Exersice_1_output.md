im copying the output here because it is not fitting on one page.

==========
SECTION: INTEGERS
==========
  Total participants: 345
  Average attendance: 86.2
  Minimum attendance: 78
  Maximum attendance: 92
==========
SECTION: STRINGS
==========

Detailed building report:
  Building A: 85 participants (Below Average)
  Building B: 92 participants (above Average)
  Building C: 78 participants (Below Average)
  Building D: 90 participants (above Average)
==========
SECTION: BOOLEANS
==========
Thresholds: expected standard > 85, minimum > 75

Simple Checks:
  Average above threshold: True
  Minimum above threshold: True
Building A: Below standard
Building B: Above standard
Building C: Below standard
Building D: Above standard
==========
SECTION: LISTS - List Operations
==========
After adding Building E:
  Building A: 85
  Building B: 92
  Building C: 78
  Building D: 90
  Building E: 88

After removing Building C:
  Building A: 85
  Building B: 92
  Building D: 90
  Building E: 88

After sorting (highest to lowest):
  Building B: 92
  Building D: 90
  Building E: 88
  Building A: 85
==========
SECTION: ARRAYS
==========
List vs Array comparison:
  Original list (first 3): [85, 92, 78]
  Python array: array('i', [85, 92, 78])
  List sum: 255
  Array sum: 255
==========
SECTION: DICTIONARIES
==========
Original Records:
  ID 1: Building A = 85 participants
  ID 2: Building B = 92 participants
  ID 3: Building C = 78 participants
  ID 4: Building D = 90 participants

Updated ID 2: Building B from 92 to 95

Deleted ID 3: Building C

After modifications:
  ID 1: Building A = 85 participants
  ID 2: Building B = 95 participants
  ID 4: Building D = 90 participants

Final Statistics:
  Total participants: 270
  Number of records: 3
  Average per record: 90.0
