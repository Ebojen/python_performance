from control.runner import calculate_total_area_control
from no_division.shapes import NO_DIVISION_CONSTRUCTORS
from utilities import  TestRunner

run_no_division = TestRunner(
    'no division',
    NO_DIVISION_CONSTRUCTORS,
    calculate_total_area_control,
)