# Öklid Mesafesi Fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Kullanıcıdan noktaları alma
points = []
print("Noktaları girmeye başlayın. Girişi bitirmek için 'q' yazın.")
while True:
    user_input = input("Bir nokta girin (örnek: x,y): ")
    if user_input.lower() == 'q':
        break
    try:
        x, y = map(float, user_input.split(","))
        points.append((x, y))
    except ValueError:
        print("Geçersiz giriş! Lütfen 'x,y' formatında bir nokta girin.")

# Noktalar arasında mesafeleri hesaplama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Minimum mesafeyi bulma ve sonuçları yazdırma
if distances:
    min_distance = min(distances)
    print("\nGirilen noktalar:", points)
    print("Minimum Öklid Mesafesi:", min_distance)
else:
    print("Mesafe hesaplanacak yeterli nokta yok.")
