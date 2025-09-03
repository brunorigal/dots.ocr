



from dots_ocr.light_parser import DotsOCRParser
from PIL import Image
import asyncio

dots_ocr_parser = DotsOCRParser(
    ip="0.0.0.0",
    port=8000,
    model_name = "dotsocr-model"
)
image = Image.open("demo/demo_image1.jpg")

result = asyncio.run(dots_ocr_parser._parse_image_vllm(image))
print(result)

import pdb;pdb.set_trace()
