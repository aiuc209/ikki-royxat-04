def ob_havo_tavsifi(harorat, namlik):
    if harorat > 25 and namlik > 60:
        return "Issiq va nam"
    elif harorat > 25 and namlik <= 60:
        return "Issiq"
    elif harorat < 10 and namlik > 60:
        return "Sovuq va nam"
    elif harorat < 10 and namlik <= 60:
        return "Sovuq"
    else:
        return "O'rtacha"

harorat = [30, 20, 5, 15, 28]
namlik = [70, 50, 80, 40, 65]

for i in range(len(harorat)):
    print(f"Harorat: {harorat[i]}C, Namlik: {namlik[i]}%, Ob-havo: {ob_havo_tavsifi(harorat[i], namlik[i])}")
