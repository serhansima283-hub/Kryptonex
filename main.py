import customtkinter as ctk
from backend import KriptoYoneticisi

ctk.set_appearance_mode("dark")

class KryptonexApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.BG_ANA = "#080A0C"
        self.BG_KART = "#0D1117"
        self.NEON = "#00FF41"
        self.KOYU_YESIL = "#008F11"
        self.GRI = "#8B949E"

        self.yonetici = KriptoYoneticisi()

        self.title("KRYPTONEX v1.0 | Şifre Çözüm Terminali")
        self.geometry("960x620")
        self.minsize(840, 540)
        self.configure(fg_color=self.BG_ANA)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu_olustur()
        self.sayfalar_olustur()
        self.sayfa_ac("cozucu")

    def menu_olustur(self):
        self.sol_panel = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color=self.BG_KART)
        self.sol_panel.grid(row=0, column=0, sticky="nsew")
        self.sol_panel.grid_propagate(False)

        ctk.CTkLabel(self.sol_panel, text="[ KRYPTONEX ]", font=("Consolas", 20, "bold"), text_color=self.NEON).pack(pady=(30, 5))
        ctk.CTkLabel(self.sol_panel, text="STATUS: ÇEVRİMİÇİ", font=("Consolas", 11), text_color=self.KOYU_YESIL).pack(pady=(0, 30))

        self.btn_cozucu = ctk.CTkButton(
            self.sol_panel, text="> Şifre Çözücü", height=40, corner_radius=2, anchor="w",
            font=("Consolas", 13, "bold"), fg_color="transparent", hover_color="#161B22",
            text_color=self.NEON, command=lambda: self.sayfa_ac("cozucu")
        )
        self.btn_cozucu.pack(fill="x", padx=15, pady=5)

        self.btn_hakkinda = ctk.CTkButton(
            self.sol_panel, text="> Sistem Bilgisi", height=40, corner_radius=2, anchor="w",
            font=("Consolas", 13, "bold"), fg_color="transparent", hover_color="#161B22",
            text_color=self.NEON, command=lambda: self.sayfa_ac("hakkinda")
        )
        self.btn_hakkinda.pack(fill="x", padx=15, pady=5)

    def sayfalar_olustur(self):
        self.sayfa_cozucu = ctk.CTkFrame(self, fg_color="transparent")

        ctk.CTkLabel(self.sayfa_cozucu, text="root@kryptonex:~/decoder# ŞİFRE ÇÖZÜCÜ", font=("Consolas", 15, "bold"), text_color=self.NEON).pack(anchor="w", padx=25, pady=(25, 15))

        ust_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color="transparent")
        ust_bar.pack(fill="x", padx=25)

        ctk.CTkLabel(ust_bar, text="[+] ŞİFRELİ METİN (GİRDİ):", font=("Consolas", 12, "bold"), text_color=self.GRI).pack(side="left")

        ctk.CTkButton(ust_bar, text="[ TEMİZLE ]", width=85, height=25, corner_radius=2, fg_color=self.BG_KART, hover_color="#1F242C", text_color="#FF5555", font=("Consolas", 11), command=self.temizle).pack(side="right", padx=(5, 0))
        ctk.CTkButton(ust_bar, text="[ YAPIŞTIR ]", width=85, height=25, corner_radius=2, fg_color=self.BG_KART, hover_color="#1F242C", text_color=self.NEON, font=("Consolas", 11), command=self.yapistir).pack(side="right")

        self.txt_input = ctk.CTkTextbox(self.sayfa_cozucu, height=130, corner_radius=2, fg_color=self.BG_KART, border_width=1, border_color=self.KOYU_YESIL, font=("Consolas", 14), text_color="#FFFFFF")
        self.txt_input.pack(fill="x", padx=25, pady=(5, 15))

        orta_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color=self.BG_KART, corner_radius=2, height=55)
        orta_bar.pack(fill="x", padx=25, pady=5)
        orta_bar.pack_propagate(False)

        ctk.CTkLabel(orta_bar, text="ALGORİTMA:", font=("Consolas", 12, "bold"), text_color=self.GRI).pack(side="left", padx=(15, 10))

        self.cmb_algoritma = ctk.CTkOptionMenu(
            orta_bar,
            values=["OTOMATİK ALGILA", "BASE64", "ONALTILIK (HEX)", "İKİLİ SİSTEM (BINARY)", "URL KODLAMA", "MORS ALFABESİ", "ROT13", "SEZAR (TÜM İHTİMALLER)"],
            width=230, height=32, corner_radius=2, fg_color=self.BG_ANA, button_color=self.KOYU_YESIL, button_hover_color=self.NEON, text_color=self.NEON, font=("Consolas", 12, "bold")
        )
        self.cmb_algoritma.pack(side="left")

        self.btn_coz = ctk.CTkButton(
            orta_bar, text=">> ŞİFREYİ ÇÖZ <<", width=180, height=34, corner_radius=2,
            fg_color=self.NEON, hover_color="#00CC33", text_color="#000000", font=("Consolas", 13, "bold"),
            command=self.coz_butonu_tiklandi
        )
        self.btn_coz.pack(side="right", padx=15)

        alt_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color="transparent")
        alt_bar.pack(fill="x", padx=25, pady=(15, 0))

        ctk.CTkLabel(alt_bar, text="[+] ÇÖZÜLEN SONUÇ (ÇIKTI):", font=("Consolas", 12, "bold"), text_color=self.NEON).pack(side="left")
        
        self.btn_kopyala = ctk.CTkButton(alt_bar, text="[ KOPYALA ]", width=110, height=25, corner_radius=2, fg_color=self.BG_KART, hover_color="#1F242C", text_color=self.NEON, font=("Consolas", 11), command=self.kopyala)
        self.btn_kopyala.pack(side="right")

        # Salt-okunur (disabled) sonuç kutusu
        self.txt_output = ctk.CTkTextbox(self.sayfa_cozucu, corner_radius=2, fg_color=self.BG_KART, border_width=1, border_color=self.NEON, font=("Consolas", 14), text_color=self.NEON, state="disabled")
        self.txt_output.pack(fill="both", expand=True, padx=25, pady=(5, 25))

        # --- HAKKINDA SAYFASI ---
        self.sayfa_hakkinda = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(self.sayfa_hakkinda, text="root@kryptonex:~/info# SİSTEM VE GELİŞTİRİCİ BİLGİLERİ", font=("Consolas", 15, "bold"), text_color=self.NEON).pack(anchor="w", padx=25, pady=(25, 15))

        kutu = ctk.CTkFrame(self.sayfa_hakkinda, fg_color=self.BG_KART, corner_radius=2, border_width=1, border_color=self.KOYU_YESIL)
        kutu.pack(fill="both", expand=True, padx=25, pady=(5, 25))

        bilgiler = [
            ("UYGULAMA ADI  :", "KRYPTONEX ŞİFRE ÇÖZÜM MERKEZİ"),
            ("SÜRÜM         :", "v1.0.0 (KARARLI SÜRÜM)"),
            ("GELİŞTİRİCİ   :", "Ahmet Serhan Şima"),
            ("MİMARİ        :", "PYTHON 3 / NESNE TABANLI PROGRAMLAMA (OOP)"),
            ("ALGORİTMALAR  :", "BASE64, HEX, BINARY, URL, MORS, ROT13, SEZAR")
        ]

        for baslik, deger in bilgiler:
            satir = ctk.CTkFrame(kutu, fg_color="transparent")
            satir.pack(fill="x", padx=25, pady=12)
            ctk.CTkLabel(satir, text=baslik, font=("Consolas", 14, "bold"), text_color=self.NEON, width=160, anchor="w").pack(side="left")
            ctk.CTkLabel(satir, text=deger, font=("Consolas", 14), text_color="#FFFFFF", anchor="w").pack(side="left")

    def sayfa_ac(self, sayfa):
        self.sayfa_cozucu.grid_forget()
        self.sayfa_hakkinda.grid_forget()
        self.btn_cozucu.configure(fg_color="transparent")
        self.btn_hakkinda.configure(fg_color="transparent")

        if sayfa == "cozucu":
            self.sayfa_cozucu.grid(row=0, column=1, sticky="nsew")
            self.btn_cozucu.configure(fg_color="#161B22")
        elif sayfa == "hakkinda":
            self.sayfa_hakkinda.grid(row=0, column=1, sticky="nsew")
            self.btn_hakkinda.configure(fg_color="#161B22")

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
import customtkinter as ctk
from backend import KriptoYoneticisi

ctk.set_appearance_mode("dark")

class KryptonexApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.BG_ANA = "#080A0C"
        self.BG_KART = "#0D1117"
        self.NEON = "#00FF41"
        self.KOYU_YESIL = "#008F11"
        self.GRI = "#8B949E"

        self.yonetici = KriptoYoneticisi()

        self.title("KRYPTONEX v1.0 | Şifre Çözüm Terminali")
        self.geometry("960x620")
        self.minsize(840, 540)
        self.configure(fg_color=self.BG_ANA)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu_olustur()
        self.sayfalar_olustur()
        self.sayfa_ac("cozucu")

    def menu_olustur(self):
        self.sol_panel = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color=self.BG_KART)
        self.sol_panel.grid(row=0, column=0, sticky="nsew")
        self.sol_panel.grid_propagate(False)

        ctk.CTkLabel(self.sol_panel, text="[ KRYPTONEX ]", font=("Consolas", 20, "bold"), text_color=self.NEON).pack(pady=(30, 5))
        ctk.CTkLabel(self.sol_panel, text="STATUS: ÇEVRİMİÇİ", font=("Consolas", 11), text_color=self.KOYU_YESIL).pack(pady=(0, 30))

        self.btn_cozucu = ctk.CTkButton(
            self.sol_panel, text="> Şifre Çözücü", height=40, corner_radius=2, anchor="w",
            font=("Consolas", 13, "bold"), fg_color="transparent", hover_color="#161B22",
            text_color=self.NEON, command=lambda: self.sayfa_ac("cozucu")
        )
        self.btn_cozucu.pack(fill="x", padx=15, pady=5)

        self.btn_hakkinda = ctk.CTkButton(
            self.sol_panel, text="> Sistem Bilgisi", height=40, corner_radius=2, anchor="w",
            font=("Consolas", 13, "bold"), fg_color="transparent", hover_color="#161B22",
            text_color=self.NEON, command=lambda: self.sayfa_ac("hakkinda")
        )
        self.btn_hakkinda.pack(fill="x", padx=15, pady=5)

    def sayfalar_olustur(self):
        self.sayfa_cozucu = ctk.CTkFrame(self, fg_color="transparent")

        ctk.CTkLabel(self.sayfa_cozucu, text="root@kryptonex:~/decoder# ŞİFRE ÇÖZÜCÜ", font=("Consolas", 15, "bold"), text_color=self.NEON).pack(anchor="w", padx=25, pady=(25, 15))

        ust_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color="transparent")
        ust_bar.pack(fill="x", padx=25)

        ctk.CTkLabel(ust_bar, text="[+] ŞİFRELİ METİN (GİRDİ):", font=("Consolas", 12, "bold"), text_color=self.GRI).pack(side="left")

        ctk.CTkButton(ust_bar, text="[ TEMİZLE ]", width=85, height=25, corner_radius=2, fg_color=self.BG_KART, hover_color="#1F242C", text_color="#FF5555", font=("Consolas", 11), command=self.temizle).pack(side="right", padx=(5, 0))
        ctk.CTkButton(ust_bar, text="[ YAPIŞTIR ]", width=85, height=25, corner_radius=2, fg_color=self.BG_KART, hover_color="#1F242C", text_color=self.NEON, font=("Consolas", 11), command=self.yapistir).pack(side="right")

        self.txt_input = ctk.CTkTextbox(self.sayfa_cozucu, height=130, corner_radius=2, fg_color=self.BG_KART, border_width=1, border_color=self.KOYU_YESIL, font=("Consolas", 14), text_color="#FFFFFF")
        self.txt_input.pack(fill="x", padx=25, pady=(5, 15))

        orta_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color=self.BG_KART, corner_radius=2, height=55)
        orta_bar.pack(fill="x", padx=25, pady=5)
        orta_bar.pack_propagate(False)

        ctk.CTkLabel(orta_bar, text="ALGORİTMA:", font=("Consolas", 12, "bold"), text_color=self.GRI).pack(side="left", padx=(15, 10))

        self.cmb_algoritma = ctk.CTkOptionMenu(
            orta_bar,
            values=["OTOMATİK ALGILA", "BASE64", "ONALTILIK (HEX)", "İKİLİ SİSTEM (BINARY)", "URL KODLAMA", "MORS ALFABESİ", "ROT13", "SEZAR (TÜM İHTİMALLER)"],
            width=230, height=32, corner_radius=2, fg_color=self.BG_ANA, button_color=self.KOYU_YESIL, button_hover_color=self.NEON, text_color=self.NEON, font=("Consolas", 12, "bold")
        )
        self.cmb_algoritma.pack(side="left")

        self.btn_coz = ctk.CTkButton(
            orta_bar, text=">> ŞİFREYİ ÇÖZ <<", width=180, height=34, corner_radius=2,
            fg_color=self.NEON, hover_color="#00CC33", text_color="#000000", font=("Consolas", 13, "bold"),
            command=self.coz_butonu_tiklandi
        )
        self.btn_coz.pack(side="right", padx=15)

        alt_bar = ctk.CTkFrame(self.sayfa_cozucu, fg_color="transparent")
        alt_bar.pack(fill="x", padx=25, pady=(15, 0))

        ctk.CTkLabel(alt_bar, text="[+] ÇÖZÜLEN SONUÇ (ÇIKTI):", font=("Consolas", 12, "bold"), text_color=self.NEON).pack(side="left")
        
        self.btn_kopyala = ctk.CTkButton(alt_bar, text="[ KOPYALA ]", width=110, height=25, corner_radius=2, fg_color=self.BG_KART, hover_color="#1F242C", text_color=self.NEON, font=("Consolas", 11), command=self.kopyala)
        self.btn_kopyala.pack(side="right")

        # Salt-okunur (disabled) sonuç kutusu
        self.txt_output = ctk.CTkTextbox(self.sayfa_cozucu, corner_radius=2, fg_color=self.BG_KART, border_width=1, border_color=self.NEON, font=("Consolas", 14), text_color=self.NEON, state="disabled")
        self.txt_output.pack(fill="both", expand=True, padx=25, pady=(5, 25))

        # --- HAKKINDA SAYFASI ---
        self.sayfa_hakkinda = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(self.sayfa_hakkinda, text="root@kryptonex:~/info# SİSTEM VE GELİŞTİRİCİ BİLGİLERİ", font=("Consolas", 15, "bold"), text_color=self.NEON).pack(anchor="w", padx=25, pady=(25, 15))

        kutu = ctk.CTkFrame(self.sayfa_hakkinda, fg_color=self.BG_KART, corner_radius=2, border_width=1, border_color=self.KOYU_YESIL)
        kutu.pack(fill="both", expand=True, padx=25, pady=(5, 25))

        bilgiler = [
            ("UYGULAMA ADI  :", "KRYPTONEX ŞİFRE ÇÖZÜM MERKEZİ"),
            ("SÜRÜM         :", "v1.0.0 (KARARLI SÜRÜM)"),
            ("GELİŞTİRİCİ   :", "Ahmet Serhan Şima"),
            ("MİMARİ        :", "PYTHON 3 / NESNE TABANLI PROGRAMLAMA (OOP)"),
            ("ALGORİTMALAR  :", "BASE64, HEX, BINARY, URL, MORS, ROT13, SEZAR")
        ]

        for baslik, deger in bilgiler:
            satir = ctk.CTkFrame(kutu, fg_color="transparent")
            satir.pack(fill="x", padx=25, pady=12)
            ctk.CTkLabel(satir, text=baslik, font=("Consolas", 14, "bold"), text_color=self.NEON, width=160, anchor="w").pack(side="left")
            ctk.CTkLabel(satir, text=deger, font=("Consolas", 14), text_color="#FFFFFF", anchor="w").pack(side="left")

    def sayfa_ac(self, sayfa):
        self.sayfa_cozucu.grid_forget()
        self.sayfa_hakkinda.grid_forget()
        self.btn_cozucu.configure(fg_color="transparent")
        self.btn_hakkinda.configure(fg_color="transparent")

        if sayfa == "cozucu":
            self.sayfa_cozucu.grid(row=0, column=1, sticky="nsew")
            self.btn_cozucu.configure(fg_color="#161B22")
        elif sayfa == "hakkinda":
            self.sayfa_hakkinda.grid(row=0, column=1, sticky="nsew")
            self.btn_hakkinda.configure(fg_color="#161B22")

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
