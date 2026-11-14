import base64
import urllib.parse
import codecs
import re

class TemelCozucu:
    def coz(self, orjinal_metin):
        raise NotImplementedError("Alt sınıflar bu metodu doldurmalıdır.")

class Base64Cozucu(TemelCozucu):
    def coz(self, orjinal_metin):
        return base64.b64decode(orjinal_metin).decode("utf-8")
    
class UrlCozucu(TemelCozucu):
    def coz(self, orjinal_metin):
        return urllib.parse.unquote(orjinal_metin)
    
class HexCozucu(TemelCozucu):
    def coz(self, orjinal_metin):
        temiz = orjinal_metin.replace(" ", "")
        return bytes.fromhex(temiz).decode("utf-8")
    
class BinaryCozucu(TemelCozucu):
    def coz(self, orjinal_metin):
        temiz = orjinal_metin.replace(" ", "")
        if len(temiz) % 8 != 0 or not re.fullmatch(r'[01]+', temiz):
            raise ValueError("Geçersiz Binary formatı")
        harfler = []
        for i in range(0, len(temiz), 8):
            parca = temiz[i:i+8]
            sayi = int(parca, 2)
            harfler.append(chr(sayi))
        return "".join(harfler)

class Rot13Cozucu(TemelCozucu):
    def coz(self, orjinal_metin):
        return codecs.decode(orjinal_metin, "rot_13")
    
class MorsCozucu(TemelCozucu):
    SOZLUK = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '/': ' '
    }
    def coz(self, orjinal_metin):
        parcalar = orjinal_metin.strip().split(" ")
        harfler = [self.SOZLUK.get(kod, "") for kod in parcalar]
        sonuc = "".join(harfler)
        if not sonuc:
            raise ValueError("Geçersiz Mors kodu")
        return sonuc
    
class SezarCozucu(TemelCozucu):
    def coz(self, orjinal_metin):
        sonuclar = []
        for anahtar in range(1, 26):
            kelime = ""
            for harf in orjinal_metin:
                if 'A' <= harf <= 'Z':
                    kelime += chr((ord(harf) - ord('A') - anahtar) % 26 + ord('A'))
                elif 'a' <= harf <= 'z':
                    kelime += chr((ord(harf) - ord('a') - anahtar) % 26 + ord('a'))
                else:
                    kelime += harf
            sonuclar.append(f"Anahtar -{anahtar:02d}: {kelime}")
        return "\n".join(sonuclar)

class KriptoYoneticisi:
    def __init__(self):
        self.algoritmalar = {
            "BASE64": Base64Cozucu(),
            "ONALTILIK (HEX)": HexCozucu(),
            "İKİLİ SİSTEM (BINARY)": BinaryCozucu(),
            "URL KODLAMA": UrlCozucu(),
            "MORS ALFABESİ": MorsCozucu(),
            "ROT13": Rot13Cozucu(),
            "SEZAR (TÜM İHTİMALLER)": SezarCozucu()
        }

    def otomatik_algila(self, metin):
        temiz = metin.strip()
        if re.fullmatch(r'[.\-/ ]+', temiz) and ('.' in temiz or '-' in temiz):
            return "MORS ALFABESİ"
        if re.fullmatch(r'[01 ]+', temiz) and len(temiz.replace(" ", "")) % 8 == 0:
            return "İKİLİ SİSTEM (BINARY)"
        if "%" in temiz and re.search(r'%[0-9A-Fa-f]{2}', temiz):
            return "URL KODLAMA"
        
        hex_aday = temiz.replace(" ", "")
        if len(hex_aday) >= 4 and len(hex_aday) % 2 == 0 and re.fullmatch(r'[0-9A-Fa-f]+', hex_aday):
            try:
                bytes.fromhex(hex_aday).decode("utf-8")
                return "ONALTILIK (HEX)"
            except Exception:
                pass

        if len(temiz) % 4 == 0 and re.fullmatch(r'[A-Za-z0-9+/]+={0,2}', temiz):
            if not temiz.isalpha() or "=" in temiz or len(temiz) >= 12:
                try:
                    sonuc = base64.b64decode(temiz).decode("utf-8")
                    if sonuc.isprintable():
                        return "BASE64"
                except Exception:
                    pass

        return "SEZAR (TÜM İHTİMALLER)"

    def islem_yap(self, metin, secim):
        metin = metin.strip()
        if not metin:
            return "[UYARI] Lütfen çözülecek bir metin girin."

        try:
            if secim == "OTOMATİK ALGILA":
                algilanan = self.otomatik_algila(metin)
                cozulen = self.algoritmalar[algilanan].coz(metin)
                return f"[OTOMATİK TESPİT: {algilanan}]\n{'-'*40}\n{cozulen}"
            else:
                cozulen = self.algoritmalar[secim].coz(metin)
                return f"[SEÇİLEN ALGORİTMA: {secim}]\n{'-'*40}\n{cozulen}"
        except Exception:
            return f"[HATA] Metin '{secim}' formatıyla çözülemedi. Formatı kontrol edin."
