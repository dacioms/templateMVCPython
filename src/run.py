#arquiteturas de software MVC (Model-View-Controller), MVVM (Model-View-ViewModel), MVP (Model-View-Presenter), MVT (Model-View-Template), MVW (Model-View-Whatever), MVU (Model-View-Update), MV* (Model-View-Any) Monolítica e Microservices SOA (Service-Oriented Architecture) e REST (Representational State Transfer) e pub/sub (publish/subscribe) e Layers 

#pyhton3 -m venv venv
#source venv/bin/activate
#pip install -r requirements.txt
#python src/run.py


#importação relativa e absoluta de módulos e pacotes em Python 3 (PEP 328 e PEP 366) e Python 2 (PEP 328 e PEP 366) 
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
# sys.path.append(str(parent))
# import src.controlers.controler as controler
# import src.models.model as model
# import src.views.view as view
# sys.path.append(str(Path(__file__).parent.parent))

