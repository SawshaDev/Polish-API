from fastapi import FastAPI, status

tags_metadata = [
   {
      "name": "Fun",
      "description": "All fun API endpoints"
   }
]

app = FastAPI(
   title="Polish API!",
   description="This API was built by Sawsha#0598 to favor his discord bot to use polish memes/gifs",
   version="1.0.0",

   openapi_tags=tags_metadata
)

import random



@app.get("/", include_in_schema=False)
async def root():
   return '''Hi! welcome to the polish API! Our current endpoint is /api/v1/poland/!'''
    


@app.get("/api/v1/poland", status_code=200, tags=["Fun"])
async def poland():
    choices = ['https://tenor.com/view/polish-power-polish-car-poland-car-strong-polish-car-gif-23408432', 'https://tenor.com/view/poland-brock-lesnar-scream-polska-poland-flag-gif-24793010', 'https://tenor.com/view/poland-i-love-poland-flag-meme-flags-gif-21735943', 'https://tenor.com/view/poland-world-cup-world-cup2018-poland-flag-gif-12036394', 'https://tenor.com/view/poland-polish-flag-gif-11055231', 'https://tenor.com/view/screenshot-poland-meme-gif-22789074', 'https://tenor.com/view/poland-gif-23540329', 'https://tenor.com/view/polish-gif-22577294']
  
    ok = random.choice(choices)

    return {"status": 200, "link": ok}


@app.get("/api/v1", include_in_schema=False)
async def api():
   return {"message":"Route not found! Please use one of our endpoints at /docs or at /api/v1/endpoints!"}

@app.get("/api/v1/endpoints", include_in_schema=False)
async def endpoints():
   return {
      "poland":{"format":"gif/png"}
   }

