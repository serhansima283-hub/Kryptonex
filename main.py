import customtkinter as ctk
import webbrowser
import platform
import os
from backend import KriptoYoneticisi

ctk.set_appearance_mode("dark")

class KryptonexApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Renk Paleti (Siber Güvenlik / Matrix Terminali)
        self.BG_ANA = "#06080A"
        self.BG_KART = "#0D1117"
        self.BG_KUTU = "#121721"
        self.NEON = "#00FF41"
        self.KOYU_YESIL = "#008F11"
        self.SARI = "#FFB000"
        self.GRI = "#8B949E"

        self.yonetici = KriptoYoneticisi()

        self.title("KRYPTONEX v1.5 | Siber Kriptografi Terminali")
        self.geometry("1080x680")
        self.minsize(940, 600)
        self.configure(fg_color=self.BG_ANA)

        # Tek pencere kesin kapanma koruması
        self.protocol("WM_DELETE_WINDOW", self.tamamen_kapat)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu_olustur()
        self.sayfalar_olustur()
        self.sayfa_ac("cozucu")

    def tamamen_kapat(self):
        self.quit()
        self.destroy()
        os._exit(0)

    def menu_olustur(self):
        self.sol_panel = ctk.CTkFrame(self, width=245, corner_radius=0, fg_color=self.BG_KART, border_width=1, border_color="#1B222C")
        self.sol_panel.grid(row=0, column=0, sticky="nsew")
        self.sol_panel.grid_propagate(False)

        # Logo & Başlık Alanı
        logo_kutu = ctk.CTkFrame(self.sol_panel, fg_color=self.BG_KUTU, corner_radius=4, border_width=1, border_color=self.KOYU_YESIL)
        logo_kutu.pack(fill="x", padx=15, pady=(25, 25))

        ctk.CTkLabel(logo_kutu, text="[ KRYPTONEX ]", font=("Consolas", 21, "bold"), text_color=self.NEON).pack(pady=(12, 2))
        ctk.CTkLabel(logo_kutu, text="● SİSTEM ÇEVRİMİÇİ", font=("Consolas", 11, "bold"), text_color=self.NEON).pack(pady=(0, 12))

        ctk.CTkLabel(self.sol_panel, text="MODÜLLER", font=("Consolas", 11, "bold"), text_color=self.GRI, anchor="w").pack(fill="x", padx=20, pady=(0, 5))

        # 1. Menü: Şifre Çözücü
        self.btn_cozucu = ctk.CTkButton(
            self.sol_panel, text="> Şifre Çözücü", height=42, corner_radius=4, anchor="w",
            font=("Consolas", 13, "bold"), fg_color="transparent", hover_color=self.BG_KUTU,
            text_color=self.NEON, command=lambda: self.sayfa_ac("cozucu")
        )
        self.btn_cozucu.pack(fill="x", padx=15, pady=4)

        # 2. Menü: Şifreleyici (Yakında)
        self.btn_sifreleyici = ctk.CTkButton(
            self.sol_panel, text="> Şifreleyici [YAKINDA]", height=42, corner_radius=4, anchor="w",
            font=("Consolas", 13, "bold"), fg_color="transparent", hover_color=self.BG_KUTU,
            text_color=self.SARI, command=lambda: self.sayfa_ac("sifreleyici")
        )
        self.btn_sifreleyici.pack(fill="x", padx=15, pady=4)

        # 3. Menü: Sistem Bilgisi
        self.btn_hakkinda = ctk.CTkButton(
            self.sol_panel, text="> Sistem Bilgisi", height=42, corner_radius=4, anchor="w",
            font=("Consolas", 13, "bold"), fg_color="transparent", hover_color=self.BG_KUTU,
            text_color=self.NEON, command=lambda: self.sayfa_ac("hakkinda")
        )
        self.btn_hakkinda.pack(fill="x", padx=15, pady=4)

        # Alt Geliştirici Kartı
        alt_kart = ctk.CTkFrame(self.sol_panel, fg_color=self.BG_KUTU, corner_radius=4, border_width=1, border_color="#1F2937")
        alt_kart.pack(side="bottom", fill="x", padx=15, pady=20)

        ctk.CTkLabel(alt_kart, text="GELİŞTİRİCİ", font=("Consolas", 10, "bold"), text_color=self.GRI).pack(pady=(8, 0))
        ctk.CTkLabel(alt_kart, text="Ahmet Serhan Şima", font=("Consolas", 12, "bold"), text_color="#FFFFFF").pack(pady=(2, 6))
        
        ctk.CTkButton(
            alt_kart, text="GITHUB PROFİLİ", height=28, corner_radius=3,
            fg_color=self.BG_KART, hover_color="#1F242C", border_width=1, border_color=self.KOYU_YESIL,
            text_color=self.NEON, font=("Consolas", 11, "bold"),
            command=lambda: webbrowser.open("https://github.com")
        ).pack(fill="x", padx=10, pady=(0, 10))

    def sayfalar_olustur(self):
        # ================= 1. ÇÖZÜCÜ SAYFASI =================
        self.sayfa_cozucu = ctk.CTkFrame(self, fg_color="transparent")

        baslik_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color=self.BG_KART, corner_radius=4, height=45, border_width=1, border_color="#1B222C")
        baslik_bar.pack(fill="x", padx=25, pady=(20, 15))
        baslik_bar.pack_propagate(False)
        ctk.CTkLabel(baslik_bar, text="root@kryptonex:~/decoder# ŞİFRE ÇÖZÜM MERKEZİ", font=("Consolas", 14, "bold"), text_color=self.NEON).pack(side="left", padx=15)
        ctk.CTkLabel(baslik_bar, text="[7 ALGORİTMA AKTİF]", font=("Consolas", 11, "bold"), text_color=self.KOYU_YESIL).pack(side="right", padx=15)

        ust_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color="transparent")
        ust_bar.pack(fill="x", padx=25)

        ctk.CTkLabel(ust_bar, text="[+] ŞİFRELİ METİN (GİRDİ):", font=("Consolas", 12, "bold"), text_color=self.GRI).pack(side="left")

        ctk.CTkButton(ust_bar, text="[ TEMİZLE ]", width=95, height=28, corner_radius=3, fg_color=self.BG_KART, hover_color="#1F242C", border_width=1, border_color="#FF5555", text_color="#FF5555", font=("Consolas", 11, "bold"), command=self.temizle).pack(side="right", padx=(6, 0))
        ctk.CTkButton(ust_bar, text="[ YAPIŞTIR ]", width=95, height=28, corner_radius=3, fg_color=self.BG_KART, hover_color="#1F242C", border_width=1, border_color=self.KOYU_YESIL, text_color=self.NEON, font=("Consolas", 11, "bold"), command=self.yapistir).pack(side="right")

        self.txt_input = ctk.CTkTextbox(self.sayfa_cozucu, height=155, corner_radius=4, fg_color=self.BG_KART, border_width=1, border_color=self.KOYU_YESIL, font=("Consolas", 14), text_color="#FFFFFF")
        self.txt_input.pack(fill="x", padx=25, pady=(6, 15))

        orta_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color=self.BG_KART, corner_radius=4, height=62, border_width=1, border_color="#1B222C")
        orta_bar.pack(fill="x", padx=25, pady=5)
        orta_bar.pack_propagate(False)

        ctk.CTkLabel(orta_bar, text="HEDEF ALGORİTMA:", font=("Consolas", 12, "bold"), text_color=self.GRI).pack(side="left", padx=(15, 10))

        self.cmb_algoritma = ctk.CTkOptionMenu(
            orta_bar,
            values=["OTOMATİK ALGILA", "BASE64", "ONALTILIK (HEX)", "İKİLİ SİSTEM (BINARY)", "URL KODLAMA", "MORS ALFABESİ", "ROT13", "SEZAR (TÜM İHTİMALLER)"],
            width=250, height=36, corner_radius=3, fg_color=self.BG_ANA, button_color=self.KOYU_YESIL, button_hover_color=self.NEON, text_color=self.NEON, font=("Consolas", 12, "bold")
        )
        self.cmb_algoritma.pack(side="left")

        self.btn_coz = ctk.CTkButton(
            orta_bar, text=">> ŞİFREYİ ÇÖZ <<", width=200, height=38, corner_radius=3,
            fg_color=self.NEON, hover_color="#00CC33", text_color="#000000", font=("Consolas", 13, "bold"),
            command=self.coz_butonu_tiklandi
        )
        self.btn_coz.pack(side="right", padx=15)

        alt_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color="transparent")
        alt_bar.pack(fill="x", padx=25, pady=(15, 0))

        ctk.CTkLabel(alt_bar, text="[+] ÇÖZÜLEN SONUÇ (ÇIKTI):", font=("Consolas", 12, "bold"), text_color=self.NEON).pack(side="left")
        
        self.btn_kopyala = ctk.CTkButton(alt_bar, text="[ KOPYALA ]", width=120, height=28, corner_radius=3, fg_color=self.BG_KART, hover_color="#1F242C", border_width=1, border_color=self.KOYU_YESIL, text_color=self.NEON, font=("Consolas", 11, "bold"), command=self.kopyala)
        self.btn_kopyala.pack(side="right")

        self.txt_output = ctk.CTkTextbox(self.sayfa_cozucu, corner_radius=4, fg_color=self.BG_KART, border_width=1, border_color=self.NEON, font=("Consolas", 14), text_color=self.NEON, state="disabled")
        self.txt_output.pack(fill="both", expand=True, padx=25, pady=(6, 20))

        # ================= 2. ŞİFRELEYİCİ (YAKINDA) SAYFASI =================
        self.sayfa_sifreleyici = ctk.CTkFrame(self, fg_color="transparent")

        sifre_baslik = ctk.CTkFrame(self.sayfa_sifreleyici, fg_color=self.BG_KART, corner_radius=4, height=45, border_width=1, border_color="#1B222C")
        sifre_baslik.pack(fill="x", padx=25, pady=(20, 15))
        sifre_baslik.pack_propagate(False)
        ctk.CTkLabel(sifre_baslik, text="root@kryptonex:~/encoder# ŞİFRELEYİCİ MODÜLÜ", font=("Consolas", 14, "bold"), text_color=self.SARI).pack(side="left", padx=15)
        ctk.CTkLabel(sifre_baslik, text="[DURUM: GELİŞTİRİLİYOR]", font=("Consolas", 11, "bold"), text_color=self.SARI).pack(side="right", padx=15)

        merkez_kutu = ctk.CTkFrame(self.sayfa_sifreleyici, fg_color=self.BG_KART, corner_radius=6, border_width=1, border_color=self.SARI)
        merkez_kutu.pack(fill="both", expand=True, padx=25, pady=(5, 20))

        ic_alan = ctk.CTkFrame(merkez_kutu, fg_color="transparent")
        ic_alan.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(ic_alan, text="[ ! ] MODÜL İNŞA AŞAMASINDA", font=("Consolas", 22, "bold"), text_color=self.SARI).pack(pady=(0, 10))
        ctk.CTkLabel(ic_alan, text="ŞİFRELEYİCİ (ENCRYPTOR) YAKINDA ARAMIZDA!", font=("Consolas", 16, "bold"), text_color="#FFFFFF").pack(pady=(0, 15))
        ctk.CTkLabel(
            ic_alan,
            text="v2.0 güncellemesi ile düz metinlerinizi tek tıkla Base64, Hex,\nBinary, URL, Mors, ROT13 ve özel anahtarlı Sezar formatlarına\ndönüştürebileceksiniz.",
            font=("Consolas", 13), text_color=self.GRI, justify="center"
        ).pack(pady=(0, 20))

        ctk.CTkButton(
            ic_alan, text="<< ŞİFRE ÇÖZÜCÜYE DÖN", width=220, height=38, corner_radius=4,
            fg_color=self.BG_KUTU, hover_color="#1F242C", border_width=1, border_color=self.NEON,
            text_color=self.NEON, font=("Consolas", 12, "bold"),
            command=lambda: self.sayfa_ac("cozucu")
        ).pack()

        # ================= 3. HAKKINDA (SİSTEM BİLGİSİ) SAYFASI =================
        self.sayfa_hakkinda = ctk.CTkFrame(self, fg_color="transparent")
        bilgi_baslik = ctk.CTkFrame(self.sayfa_hakkinda, fg_color=self.BG_KART, corner_radius=4, height=45, border_width=1, border_color="#1B222C")
        bilgi_baslik.pack(fill="x", padx=25, pady=(20, 15))
        bilgi_baslik.pack_propagate(False)
        ctk.CTkLabel(bilgi_baslik, text="root@kryptonex:~/info# SİSTEM VE GELİŞTİRİCİ BİLGİLERİ", font=("Consolas", 14, "bold"), text_color=self.NEON).pack(side="left", padx=15)
        
        kutu = ctk.CTkFrame(self.sayfa_hakkinda, fg_color=self.BG_KART, corner_radius=4, border_width=1, border_color=self.KOYU_YESIL)
        kutu.pack(fill="both", expand=True, padx=25, pady=(5, 20))
        
        isletim_sistemi = f"{platform.system()} {platform.release()} ({platform.machine()})"
        bilgiler = [
            ("UYGULAMA ADI   :", "KRYPTONEX ŞİFRE ÇÖZÜM MERKEZİ"),
            ("SÜRÜM          :", "v1.5.0 (MODERN TERMİNAL SÜRÜMÜ)"),
            ("GELİŞTİRİCİ    :", "Ahmet Serhan Şima"),
            ("GİTHUB ADRESİ  :", "github.com"),
            ("MİMARİ         :", "PYTHON 3 / NESNE TABANLI PROGRAMLAMA (OOP)"),
            ("ALGORİTMALAR   :", "BASE64, HEX, BINARY, URL, MORS, ROT13, SEZAR"),
            ("AKTİF SİSTEM   :", isletim_sistemi)
        ]
        
        for baslik, deger in bilgiler:
            satir = ctk.CTkFrame(kutu, fg_color="transparent")
            satir.pack(fill="x", padx=30, pady=12)
            ctk.CTkLabel(satir, text=baslik, font=("Consolas", 14, "bold"), text_color=self.NEON, width=170, anchor="w").pack(side="left")
            if "github.com" in deger:
                link = ctk.CTkLabel(satir, text=deger, font=("Consolas", 14, "underline"), text_color=self.NEON, cursor="hand2", anchor="w")
                link.pack(side="left")
                link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com"))
            else:
                ctk.CTkLabel(satir, text=deger, font=("Consolas", 14), text_color="#FFFFFF", anchor="w").pack(side="left")

    def sayfa_ac(self, sayfa):
        self.sayfa_cozucu.grid_forget()
        self.sayfa_sifreleyici.grid_forget()
        self.sayfa_hakkinda.grid_forget()
        
        self.btn_cozucu.configure(fg_color="transparent")
        self.btn_sifreleyici.configure(fg_color="transparent")
        self.btn_hakkinda.configure(fg_color="transparent")
        
        if sayfa == "cozucu":
            self.sayfa_cozucu.grid(row=0, column=1, sticky="nsew")
            self.btn_cozucu.configure(fg_color=self.BG_KUTU)
        elif sayfa == "sifreleyici":
            self.sayfa_sifreleyici.grid(row=0, column=1, sticky="nsew")
            self.btn_sifreleyici.configure(fg_color=self.BG_KUTU)
        elif sayfa == "hakkinda":
            self.sayfa_hakkinda.grid(row=0, column=1, sticky="nsew")
            self.btn_hakkinda.configure(fg_color=self.BG_KUTU)

    def cikti_yaz(self, metin):
        self.txt_output.configure(state="normal")
        self.txt_output.delete("1.0", "end")
        self.txt_output.insert("1.0", metin)
        self.txt_output.configure(state="disabled")

    def coz_butonu_tiklandi(self):
        girdi = self.txt_input.get("1.0", "end-1c")
        secim = self.cmb_algoritma.get()
        sonuc = self.yonetici.islem_yap(girdi, secim)
        self.cikti_yaz(sonuc)

    def yapistir(self):
        try:
            self.txt_input.delete("1.0", "end")
            self.txt_input.insert("1.0", self.clipboard_get())
        except Exception:
            pass

    def temizle(self):
        self.txt_input.delete("1.0", "end")
        self.cikti_yaz("")

    def kopyala(self):
        veri = self.txt_output.get("1.0", "end-1c")
        if veri:
            self.clipboard_clear()
            self.clipboard_append(veri)
            self.btn_kopyala.configure(text="[ ✓ KOPYALANDI ]")
            self.after(1500, lambda: self.btn_kopyala.configure(text="[ KOPYALA ]"))

if __name__ == "__main__":
    app = KryptonexApp()
    app.mainloop()
