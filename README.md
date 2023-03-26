# Voice-Cloning-MircoService

```
This MicroService Work on Conda python 3.7
```
## Notes
The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```
- Requirements

```
# Fast API Packages
fastapi==0.71.0
uvicorn[standard]==0.16.0
pyjwt==2.3.0
python-multipart==0.0.5

# Application Packages
inflect==6.0.2
librosa==0.8.1
matplotlib==3.5.1
numpy==1.20.3
Pillow==8.4.0
PyQt5==5.15.6
scikit-learn==1.0.2
scipy==1.7.3
sounddevice==0.4.3
SoundFile==0.10.3.post1
tqdm==4.62.3
umap-learn==0.5.2
Unidecode==1.3.2
urllib3==1.26.7
visdom==0.1.8.9
webrtcvad-wheels==2.0.11.post1

# Pytorch requirements
torch
torchvision
torchaudio

pydub


```

The base Binder image contains no extra dependencies, so be as
explicit as possible in defining the packages that you need. This includes
specifying explicit versions wherever possible.

If you do specify strict versions, it is important to do so for *all*
your dependencies, not just direct dependencies.
Strictly specifying only some dependencies is a recipe for environments
breaking over time.

[pip-compile](https://github.com/jazzband/pip-tools/) is a handy
tool for combining loosely specified dependencies with a fully frozen environment.
You write a requirements.in with just the dependencies you need
and pip-compile will generate a requirements.txt with all the strict packages and versions that would come from installing that package right now.
That way, you only need to specify what you actually know you need,
but you also get a snapshot of your environment.

In this example we include the library `seaborn` which will be installed in
the environment, and our notebook uses it to plot a figure.
