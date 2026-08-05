import barcode
from barcode.writer import ImageWriter


def generate_barcode(data):
    try:
        barcode_type = barcode.get_barcode_class("code128")

        barcode_image = barcode_type(
            data,
            writer=ImageWriter()
        )

        filename = barcode_image.save("generated_barcode")

        print("✅ Barcode generated successfully!")
        print(f"📁 Saved as: {filename}")

    except Exception as e:
        print("❌ Error:", e)


print("===== Barcode Generator =====")

user_data = input("Enter text or number to generate barcode: ")

if user_data.strip():
    generate_barcode(user_data)
else:
    print("❌ Input cannot be empty.")