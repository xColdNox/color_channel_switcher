from PIL import Image
from numpy import zeros,asarray,uint8

def kanaly(plik,kanaly):
    obraz = Image.open(plik)
    obrazjakotablica=asarray(obraz)
    print(obrazjakotablica.shape)
    wynikowy=zeros([obrazjakotablica.shape[0], obrazjakotablica.shape[1],3])
    wynikowy=zeros(obrazjakotablica.shape)
    
    wynikowy[:,:,0]=obrazjakotablica[:,:,kanaly[0]]
    wynikowy[:,:,1]=obrazjakotablica[:,:,kanaly[1]]
    wynikowy[:,:,2]=obrazjakotablica[:,:,kanaly[2]]
    
    return Image.fromarray(uint8(wynikowy))
    
if __name__=="__main__":
    plik = "./pies.jpg"
    rezultat=kanaly(plik,[0,1,0])
    rezultat.save("Rezultat1.jpg")
    
    rezultat=kanaly(plik,[2,0,0])
    rezultat.save("Rezultat2.jpg")
    
    rezultat=kanaly(plik,[1,2,1])
    rezultat.save("Rezultat3.jpg")