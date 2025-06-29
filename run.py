# run.py
import sys, os
# garante que o diretório local seja buscado primeiro
sys.path.insert(0, os.path.dirname(__file__))
from streamlit.web.cli import main
if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py"]
    main()
