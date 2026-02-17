import ezdxf
import numpy as np
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Gigantyczny słownik języków
LANGUAGES = {
    "Polski": {
        "title": "Generator Zembatek", "params": "PARAMETRY", "mod": "Moduł", "teeth": "Liczba zębów",
        "alpha": "Kąt przyporu (°)", "hole": "Otwór wału (mm)", "update": "Aktualizuj Podgląd",
        "save_dxf": "Zapisz DXF (CAD)", "save_svg": "Zapisz SVG (Laser)", "pitch": "Śr. podziałowa",
        "outer": "Śr. zewnętrzna", "root": "Śr. dna", "success": "Sukces", "msg_saved": "Zapisano pomyślnie!", "error": "Błąd"
    },
    "English": {
        "title": "Gear Generator", "params": "PARAMETERS", "mod": "Module", "teeth": "Number of teeth",
        "alpha": "Pressure angle (°)", "hole": "Shaft hole (mm)", "update": "Update Preview",
        "save_dxf": "Save DXF", "save_svg": "Save SVG", "pitch": "Pitch diameter",
        "outer": "Outer diameter", "root": "Root diameter", "success": "Success", "msg_saved": "Saved successfully!", "error": "Error"
    },
    "Deutsch": {
        "title": "Zahnrad-Generator", "params": "PARAMETER", "mod": "Modul", "teeth": "Zähnezahl",
        "alpha": "Eingriffswinkel (°)", "hole": "Bohrung (mm)", "update": "Vorschau",
        "save_dxf": "DXF speichern", "save_svg": "SVG speichern", "pitch": "Teilkreis",
        "outer": "Kopfkreis", "root": "Fußkreis", "success": "Erfolg", "msg_saved": "Gespeichert!", "error": "Fehler"
    },
    "Français": {
        "title": "Générateur d'engrenages", "params": "PARAMÈTRES", "mod": "Module", "teeth": "Nombre de dents",
        "alpha": "Angle de pression", "hole": "Trou d'arbre", "update": "Mettre à jour",
        "save_dxf": "Enregistrer DXF", "save_svg": "Enregistrer SVG", "pitch": "Diamètre primitif",
        "outer": "Diamètre de tête", "root": "Diamètre de pied", "success": "Succès", "msg_saved": "Enregistré !", "error": "Erreur"
    },
    "Italiano": {
        "title": "Generatore di ingranaggi", "params": "PARAMETRI", "mod": "Modulo", "teeth": "Denti",
        "alpha": "Angolo di pressione", "hole": "Foro", "update": "Aggiorna",
        "save_dxf": "Salva DXF", "save_svg": "Salva SVG", "pitch": "Diametro primitivo",
        "outer": "Diametro esterno", "root": "Diametro radice", "success": "Successo", "msg_saved": "Salvato!", "error": "Errore"
    },
    "Español": {
        "title": "Generador de engranajes", "params": "PARÁMETROS", "mod": "Módulo", "teeth": "Dientes",
        "alpha": "Ángulo de presión", "hole": "Agujero", "update": "Actualizar",
        "save_dxf": "Guardar DXF", "save_svg": "Guardar SVG", "pitch": "Diámetro primitivo",
        "outer": "Diámetro exterior", "root": "Diámetro raíz", "success": "Éxito", "msg_saved": "¡Guardado!", "error": "Error"
    },
    "Português": {
        "title": "Gerador de engrenagens", "params": "PARÂMETROS", "mod": "Módulo", "teeth": "Dentes",
        "alpha": "Ângulo", "hole": "Furo", "update": "Atualizar",
        "save_dxf": "Salvar DXF", "save_svg": "Salvar SVG", "pitch": "Diâmetro primitivo",
        "outer": "Diâmetro externo", "root": "Diâmetro raiz", "success": "Sucesso", "msg_saved": "Salvo!", "error": "Erro"
    },
    "Русский": {
        "title": "Генератор шестерен", "params": "ПАРАМЕТРЫ", "mod": "Модуль", "teeth": "Зубья",
        "alpha": "Угол профиля", "hole": "Отверстие", "update": "Обновить",
        "save_dxf": "Сохранить DXF", "save_svg": "Сохранить SVG", "pitch": "Делительный Ø",
        "outer": "Внешний Ø", "root": "Впадин Ø", "success": "Успех", "msg_saved": "Сохранено!", "error": "Ошибка"
    },
    "Українська": {
        "title": "Генератор шестерень", "params": "ПАРАМЕТРИ", "mod": "Модуль", "teeth": "Зуби",
        "alpha": "Кут зачеплення", "hole": "Отвір", "update": "Оновити",
        "save_dxf": "Зберегти DXF", "save_svg": "Зберегти SVG", "pitch": "Дільничний Ø",
        "outer": "Зовнішній Ø", "root": "Впадин Ø", "success": "Успіх", "msg_saved": "Збережено!", "error": "Помилка"
    },
    "日本語": {
        "title": "歯車ジェネレーター", "params": "パラメーター", "mod": "モジュール", "teeth": "歯数",
        "alpha": "圧力角", "hole": "軸穴", "update": "更新",
        "save_dxf": "DXF保存", "save_svg": "SVG保存", "pitch": "ピッチ円径",
        "outer": "歯先円径", "root": "歯底円径", "success": "成功", "msg_saved": "保存完了", "error": "エラー"
    },
    "中文": {
        "title": "齿轮生成器", "params": "参数设置", "mod": "模数", "teeth": "齿数",
        "alpha": "压力角", "hole": "轴孔径", "update": "刷新预览",
        "save_dxf": "保存 DXF", "save_svg": "保存 SVG", "pitch": "分度圆直径",
        "outer": "齿顶圆直径", "root": "齿根圆直径", "success": "成功", "msg_saved": "保存成功！", "error": "错误"
    },
    "한국어": {
        "title": "기어 생성기", "params": "매개변수", "mod": "모듈", "teeth": "이빨 수",
        "alpha": "압력각", "hole": "샤프트 직경", "update": "새로고침",
        "save_dxf": "DXF 저장", "save_svg": "SVG 저장", "pitch": "피치원 지름",
        "outer": "이끝원 지름", "root": "이뿌리원 지름", "success": "성공", "msg_saved": "저장되었습니다!", "error": "오류"
    },
    "Türkçe": {
        "title": "Dişli Oluşturucu", "params": "PARAMETRELER", "mod": "Modül", "teeth": "Diş Sayısı",
        "alpha": "Basınç Açısı", "hole": "Mil Deliği", "update": "Güncelle",
        "save_dxf": "DXF Kaydet", "save_svg": "SVG Kaydet", "pitch": "Bölüm Dairesi",
        "outer": "Diş Üstü Çapı", "root": "Diş Dibi Çapı", "success": "Başarılı", "msg_saved": "Kaydedildi!", "error": "Hata"
    },
    "العربية": {
        "title": "مولد التروس", "params": "المعلمات", "mod": "الموديول", "teeth": "عدد الأسنان",
        "alpha": "زاوية الضغط", "hole": "قطر الثقب", "update": "تحديث",
        "save_dxf": "حفظ DXF", "save_svg": "حفظ SVG", "pitch": "قطر الخطوة",
        "outer": "القطر الخارجي", "root": "قطر الجذر", "success": "نجاح", "msg_saved": "تم الحفظ!", "error": "خطأ"
    },
    "Tiếng Việt": {
        "title": "Máy phát bánh răng", "params": "THÔNG SỐ", "mod": "Mô-đun", "teeth": "Số răng",
        "alpha": "Góc áp lực", "hole": "Lỗ trục", "update": "Cập nhật",
        "save_dxf": "Lưu DXF", "save_svg": "Lưu SVG", "pitch": "Đường kính vòng chia",
        "outer": "Đường kính đỉnh", "root": "Đường kính chân", "success": "Thành công", "msg_saved": "Đã lưu!", "error": "Lỗi"
    }
}

# --- LOGIKA GEOMETRII ---
def calculate_gear_geometry(module, teeth, pressure_angle):
    pitch_rad = (module * teeth) / 2
    base_rad = pitch_rad * np.cos(np.radians(pressure_angle))
    outer_rad = pitch_rad + module
    root_rad = pitch_rad - 1.25 * module
    inv_alpha = np.tan(np.radians(pressure_angle)) - np.radians(pressure_angle)
    half_tooth_angle = (np.pi / (2 * teeth)) + inv_alpha
    
    all_points = []
    for i in range(teeth):
        angle_offset = (2 * np.pi * i) / teeth
        side1 = []
        for t in np.linspace(0, 0.7, 25):
            x = base_rad * (np.cos(t) + t * np.sin(t))
            y = base_rad * (np.sin(t) - t * np.cos(t))
            r = np.hypot(x, y)
            phi = np.arctan2(y, x) + angle_offset + half_tooth_angle
            curr_r = max(root_rad, min(r, outer_rad))
            side1.append((curr_r * np.cos(phi), curr_r * np.sin(phi)))
            if r >= outer_rad: break
        side2 = []
        for p in reversed(side1):
            r = np.hypot(p[0], p[1])
            phi = np.arctan2(p[1], p[0])
            mirror_phi = 2 * angle_offset - phi
            side2.append((r * np.cos(mirror_phi), r * np.sin(mirror_phi)))
        gap_phi = (angle_offset + (2 * np.pi * (i + 1)) / teeth) / 2
        all_points.extend(side1)
        all_points.extend(side2)
        all_points.append((root_rad * np.cos(gap_phi), root_rad * np.sin(gap_phi)))
    return all_points, pitch_rad, outer_rad, root_rad

# --- INTERFEJS ---
class GearApp:
    def __init__(self, root):
        self.root = root
        self.current_lang = "Polski"
        self.root.geometry("1100x750")
        
        # Stylizacja panelu
        self.ctrl_frame = tk.Frame(root, padx=20, pady=20, bg="#f0f0f0", relief="ridge", borderwidth=2)
        self.ctrl_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        tk.Label(self.ctrl_frame, text="Select Language:", bg="#f0f0f0").pack(anchor="w")
        self.lang_combo = ttk.Combobox(self.ctrl_frame, values=list(LANGUAGES.keys()), state="readonly")
        self.lang_combo.set("Polski")
        self.lang_combo.pack(pady=(0, 20), fill=tk.X)
        self.lang_combo.bind("<<ComboboxSelected>>", self.change_language)

        self.lbl_params = tk.Label(self.ctrl_frame, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.lbl_params.pack(pady=10)

        self.labels = {}
        self.vars = {
            "mod": tk.DoubleVar(value=2.0), "teeth": tk.IntVar(value=18),
            "alpha": tk.DoubleVar(value=20.0), "hole": tk.DoubleVar(value=8.0)
        }

        for key in self.vars:
            self.labels[key] = tk.Label(self.ctrl_frame, text="", bg="#f0f0f0")
            self.labels[key].pack(anchor="w")
            tk.Entry(self.ctrl_frame, textvariable=self.vars[key]).pack(pady=2, fill=tk.X)

        self.btn_update = tk.Button(self.ctrl_frame, text="", command=self.update_plot, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        self.btn_update.pack(fill=tk.X, pady=(20, 5))
        
        self.btn_dxf = tk.Button(self.ctrl_frame, text="", command=self.save_dxf, bg="#4CAF50", fg="white")
        self.btn_dxf.pack(fill=tk.X, pady=2)
        
        self.btn_svg = tk.Button(self.ctrl_frame, text="", command=self.save_svg, bg="#FF9800", fg="white")
        self.btn_svg.pack(fill=tk.X, pady=2)
        
        self.info_box = tk.Label(self.ctrl_frame, text="", justify=tk.LEFT, font=("Courier New", 10), bg="white", relief="sunken", padx=10, pady=10)
        self.info_box.pack(pady=30, fill=tk.X)
        
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.change_language()

    def change_language(self, event=None):
        self.current_lang = self.lang_combo.get()
        l = LANGUAGES[self.current_lang]
        self.root.title(l["title"])
        self.lbl_params.config(text=l["params"])
        self.labels["mod"].config(text=l["mod"])
        self.labels["teeth"].config(text=l["teeth"])
        self.labels["alpha"].config(text=l["alpha"])
        self.labels["hole"].config(text=l["hole"])
        self.btn_update.config(text=l["update"])
        self.btn_dxf.config(text=l["save_dxf"])
        self.btn_svg.config(text=l["save_svg"])
        self.update_plot()

    def update_plot(self):
        try:
            m, z, a, h = self.vars["mod"].get(), self.vars["teeth"].get(), self.vars["alpha"].get(), self.vars["hole"].get()
            pts, pr, orad, rrad = calculate_gear_geometry(m, z, a)
            self.ax.clear()
            x, y = zip(*(pts + [pts[0]]))
            self.ax.plot(x, y, color='#1f77b4', lw=2)
            self.ax.add_artist(plt.Circle((0, 0), pr, color='red', ls='--', fill=False, alpha=0.4))
            self.ax.add_artist(plt.Circle((0, 0), h/2, color='black', fill=False))
            self.ax.set_aspect('equal')
            l = LANGUAGES[self.current_lang]
            info = f"{l['pitch']}: {2*pr:.2f} mm\n{l['outer']}: {2*orad:.2f} mm\n{l['root']}: {2*rrad:.2f} mm"
            self.info_box.config(text=info)
            self.canvas.draw()
        except: pass

    def save_dxf(self):
        l = LANGUAGES[self.current_lang]
        path = filedialog.asksaveasfilename(defaultextension=".dxf", filetypes=[("AutoCAD DXF", "*.dxf")])
        if not path: return
        try:
            doc = ezdxf.new('R2010'); doc.header['$INSUNITS'] = 4; msp = doc.modelspace()
            pts, _, _, _ = calculate_gear_geometry(self.vars["mod"].get(), self.vars["teeth"].get(), self.vars["alpha"].get())
            msp.add_lwpolyline(pts, close=True)
            if self.vars["hole"].get() > 0: msp.add_circle((0, 0), radius=self.vars["hole"].get()/2)
            doc.saveas(path)
            messagebox.showinfo(l["success"], l["msg_saved"])
        except Exception as e: messagebox.showerror(l["error"], str(e))

    def save_svg(self):
        l = LANGUAGES[self.current_lang]
        path = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("Vector SVG", "*.svg")])
        if not path: return
        try:
            pts, _, orad, _ = calculate_gear_geometry(self.vars["mod"].get(), self.vars["teeth"].get(), self.vars["alpha"].get())
            scale, off = 5, (orad * 5) + 20
            with open(path, "w", encoding="utf-8") as f:
                f.write(f'<svg width="{off*2}" height="{off*2}" xmlns="http://www.w3.org/2000/svg">\n')
                pts_str = " ".join([f"{p[0]*scale+off},{p[1]*scale+off}" for p in pts])
                f.write(f'  <polygon points="{pts_str}" fill="#e1f5fe" stroke="#01579b" stroke-width="2" />\n')
                f.write(f'  <circle cx="{off}" cy="{off}" r="{(self.vars["hole"].get()/2)*scale}" fill="white" stroke="black" />\n')
                f.write(f'</svg>')
            messagebox.showinfo(l["success"], l["msg_saved"])
        except Exception as e: messagebox.showerror(l["error"], str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = GearApp(root)
    root.mainloop()