from fastapi import FastAPI
from fastapi import File, UploadFile
from clip_interrogator import Config, Interrogator

clip_model_name = "ViT-L-14/openai"
app = FastAPI()
clip_config = Config()
clip_config.blip_num_beams = 64
clip_config.blip_offload = False
clip_config.cache_path = "./model-cache"
clip_config.clip_model_name = clip_model_name
ci = Interrogator(clip_config)


@app.get("/")
def read_image(file: UploadFile = File(...)):
	return ci.interrogate(file.file)
