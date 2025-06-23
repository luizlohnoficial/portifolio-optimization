import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from quantum_portfolio.main import main

def test_main_runs():
    result = main()
    assert hasattr(result, "fval")
