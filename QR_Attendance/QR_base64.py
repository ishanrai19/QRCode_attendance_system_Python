import os
from MyQR import myqr
import base64

# read text file
f=open('./students.txt','r')
lines = f.read().split("\n")
print(lines)

"""
for i in range(0,len(lines)):
    print(31)
    def create_code():
        input_path=filedialog.asksaveasfilename(title="Save Image", filetype=(("PNG File",png),("All Files","*.*")))
        if input_path:
            if input_path.endswith(".png"):
                get_code=pyqrcode.create(lines[i].encode)
                get_code.png(input_path,scale=5)
            else:
                input_path=f'{input_path}.png'
                get_code=pyqrcode.create(lines[i].encode)
                get_code.png(input_path,scale=5)
"""

# create qr code
for i in range(0,len(lines)):
    data = lines[i].encode()
    name=base64.b64encode(data)
    name.config(text=f"{data[0].data.decode('ascii')}")

    version,level,qr_name = myqr.run(
        str(name),
        level = 'H',
        version=1,
        picture="./white.jpg",
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name = str(lines[i]+'.png'),
        save_dir=os.getcwd()

    )



