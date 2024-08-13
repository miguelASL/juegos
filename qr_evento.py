import qrcode
from PIL import Image, ImageDraw, ImageFont

def create_qr_code(text, output_filename):
    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Add a label to the QR code
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except IOError:
        font = ImageFont.load_default()
    label_pos = (10, img.size[1] - 20)  # position for the label at the bottom
    draw.text(label_pos, text, font=font, fill="black")
    
    # Save the QR code
    img.save(output_filename)

def generate_qr_code_for_guest(guest_list):
    for index, guest in enumerate(guest_list, start=1):
        guest_name = guest["name"]
        qr_data = f"Invitado: {guest_name}\nID: {index}\nBienvenido a la charla de análisis de datos de Miguel Sarmiento!"
        output_filename = f"guest_{index}.jpg"
        
        create_qr_code(qr_data, output_filename)
        print(f"Generating QR code for {guest_name}...")

# Lista de invitados
guest_list = [
    {"name": "Alice"},
    {"name": "Bob"}
]

generate_qr_code_for_guest(guest_list)