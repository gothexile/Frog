import discord
from discord.ext import commands 

import os, shutil
from google_images_download import google_images_download
import random

class image_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.download_folder = 'downloads'
        
        self.keywords = 'frog' 
        
        self.response = google_images_download.googleimagesdownload()

        self.arguments = {
            "keywords": self.keywords,
            "limit": 40,
            "size": "medium",
            "no_directory": True
        }

        self.image_names = []
        self.update_images()
       

    def update_images(self):
        for filename in os.listdir(self.download_folder):
            self.image_names.append(os.path.join(self.download_folder, filename))

    def clear_folder(self):
        for filename in os.listdir(self.download_folder):
            file_path = os.path.join(self.download_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print("Failed to delete %s. reason %s" % (file_path, e))
    
    @commands.command()
    async def frog(self, ctx):
        images_size = len(self.image_names)
        random_image = random.randint(0, images_size)
        img_path = self.image_names[random_image]

        await ctx.send(file=discord.File(img_path))

        self.clear_folder()
        search_args = "frog"
        self.arguments['keywords'] = search_args
        
        self.response.download(self.arguments)

        self.update_images()




        
     
