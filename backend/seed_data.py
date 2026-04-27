from message_generator import generate_message

B2B_PARTNERS = [
    # Navigation
    {"company_name": "2GIS Казахстан", "category": "Навигация", "website": "2gis.kz", "contact_name": "Команда партнёрств", "contact_email": "partners@2gis.ru", "contact_linkedin": "linkedin.com/company/2gis", "priority": "high", "use_case": "Озвучка навигационных подсказок на казахском языке"},
    {"company_name": "Yandex Maps KZ", "category": "Навигация", "website": "yandex.kz/maps", "contact_email": "business@yandex.kz", "contact_linkedin": "linkedin.com/company/yandex", "priority": "high", "use_case": "Казахскоязычный TTS для навигации"},
    # Fintech / Banks
    {"company_name": "Kaspi.kz", "category": "Финтех / Банки", "website": "kaspi.kz", "contact_name": "Михаил Ломтадзе", "contact_position": "CEO", "contact_linkedin": "linkedin.com/in/mikhail-lomtadze", "contact_email": "info@kaspi.kz", "priority": "high", "use_case": "Голосовой ассистент в суперприложении Kaspi на казахском"},
    {"company_name": "Halyk Bank", "category": "Финтех / Банки", "website": "halykbank.kz", "contact_name": "Умут Шаяхметова", "contact_position": "CEO", "contact_linkedin": "linkedin.com/in/umut-shayakhmetova", "contact_email": "info@halykbank.kz", "contact_phone": "+7 727 259 04 40", "priority": "high", "use_case": "IVR и голосовые уведомления на казахском"},
    {"company_name": "Forte Bank", "category": "Финтех / Банки", "website": "forte.kz", "contact_email": "info@forte.kz", "contact_phone": "+7 727 311 11 00", "contact_linkedin": "linkedin.com/company/fortebank", "priority": "medium", "use_case": "Обновление IVR с казахским TTS"},
    {"company_name": "Jusan Bank", "category": "Финтех / Банки", "website": "jusan.kz", "contact_email": "info@jusan.kz", "contact_linkedin": "linkedin.com/company/jusan-bank", "priority": "medium", "use_case": "Голосовой банкинг на казахском языке"},
    {"company_name": "Freedom Finance Bank", "category": "Финтех / Банки", "website": "ffbank.kz", "contact_email": "bank@ffin.kz", "contact_linkedin": "linkedin.com/company/freedom-finance-bank", "priority": "medium", "use_case": "TTS для мобильного банка и IVR"},
    {"company_name": "Bank RBK", "category": "Финтех / Банки", "website": "bankrbk.kz", "contact_email": "info@bankrbk.kz", "contact_phone": "+7 727 311 00 11", "priority": "low", "use_case": "Голосовые уведомления клиентам"},
    # Telecom
    {"company_name": "Kazakhtelecom", "category": "Телеком", "website": "telecom.kz", "contact_email": "info@telecom.kz", "contact_phone": "+7 727 258 88 88", "contact_linkedin": "linkedin.com/company/kazakhtelecom", "priority": "high", "use_case": "IVR модернизация и голосовые сервисы на казахском"},
    {"company_name": "Kcell", "category": "Телеком", "website": "kcell.kz", "contact_email": "b2b@kcell.kz", "contact_phone": "+7 727 258 00 58", "contact_linkedin": "linkedin.com/company/kcell", "priority": "high", "use_case": "IVR и голосовые уведомления абонентам"},
    {"company_name": "Beeline Казахстан", "category": "Телеком", "website": "beeline.kz", "contact_email": "b2b@beeline.kz", "contact_linkedin": "linkedin.com/company/beeline-kazakhstan", "priority": "high", "use_case": "Казахскоязычный IVR и автоинформатор"},
    {"company_name": "Tele2 Казахстан", "category": "Телеком", "website": "tele2.kz", "contact_email": "info@tele2.kz", "contact_linkedin": "linkedin.com/company/tele2-kazakhstan", "priority": "medium", "use_case": "Голосовые сервисы для абонентов"},
    # EdTech
    {"company_name": "Bilim Land", "category": "EdTech / Образование", "website": "bilimland.kz", "contact_name": "Асель Жаксыбекова", "contact_position": "CEO", "contact_linkedin": "linkedin.com/in/assel-zhaksybekova", "contact_email": "info@bilimland.kz", "priority": "high", "use_case": "Озвучка уроков и проверка произношения на казахском"},
    {"company_name": "Salam Tili", "category": "EdTech / Образование", "website": "salamtili.kz", "contact_email": "info@salamtili.kz", "contact_telegram": "@salamtili", "priority": "high", "use_case": "TTS для произношения и STT для проверки речи в приложении"},
    {"company_name": "Kundelik.kz", "category": "EdTech / Образование", "website": "kundelik.kz", "contact_email": "support@kundelik.kz", "contact_linkedin": "linkedin.com/company/kundelik", "priority": "medium", "use_case": "Голосовые уведомления и озвучка заданий"},
    {"company_name": "SXODIM (Oqy.kz)", "category": "EdTech / Образование", "website": "oqy.kz", "contact_email": "info@oqy.kz", "priority": "medium", "use_case": "Казахский TTS для онлайн-обучения"},
    # Marketplace
    {"company_name": "Kolesa.kz", "category": "Маркетплейс", "website": "kolesa.kz", "contact_email": "info@kolesa.kz", "contact_linkedin": "linkedin.com/company/kolesa-kz", "priority": "medium", "use_case": "Голосовой поиск авто и уведомления"},
    {"company_name": "Krisha.kz", "category": "Маркетплейс", "website": "krisha.kz", "contact_email": "info@krisha.kz", "priority": "medium", "use_case": "Голосовой поиск недвижимости"},
    {"company_name": "OLX Казахстан", "category": "Маркетплейс", "website": "olx.kz", "contact_linkedin": "linkedin.com/company/olx-group", "priority": "low", "use_case": "Голосовой поиск объявлений на казахском"},
    # Delivery
    {"company_name": "Choco.kz", "category": "Доставка / Логистика", "website": "choco.kz", "contact_email": "info@choco.kz", "contact_linkedin": "linkedin.com/company/chocofamily", "priority": "medium", "use_case": "Голосовые уведомления о заказах на казахском"},
    {"company_name": "Kazpost", "category": "Доставка / Логистика", "website": "kazpost.kz", "contact_email": "info@kazpost.kz", "contact_phone": "+7 727 258 03 70", "priority": "medium", "use_case": "Голосовые уведомления о посылках"},
    {"company_name": "Glovo Казахстан", "category": "Доставка / Логистика", "website": "glovoapp.com", "contact_linkedin": "linkedin.com/company/glovo-app", "priority": "low", "use_case": "Уведомления о доставке на казахском"},
    # GovTech
    {"company_name": "eGov.kz", "category": "Гос. технологии", "website": "egov.kz", "contact_email": "info@nitec.kz", "contact_phone": "+7 727 258 80 80", "contact_linkedin": "linkedin.com/company/nitec", "priority": "high", "use_case": "Голосовой ассистент госуслуг на казахском языке"},
    {"company_name": "НИТ (МЦРИАП)", "category": "Гос. технологии", "website": "nitec.kz", "contact_email": "info@nitec.kz", "contact_linkedin": "linkedin.com/company/nitec", "priority": "high", "use_case": "ИИ-голосовые сервисы для цифрового правительства"},
    # Healthcare
    {"company_name": "MedElement", "category": "Здравоохранение", "website": "medelement.com", "contact_email": "info@medelement.com", "contact_linkedin": "linkedin.com/company/medelement", "priority": "medium", "use_case": "Голосовые напоминания пациентам и IVR клиник"},
    {"company_name": "Docmed.kz", "category": "Здравоохранение", "website": "docmed.kz", "contact_email": "info@docmed.kz", "priority": "medium", "use_case": "Голосовая запись к врачу на казахском"},
    # Aviation
    {"company_name": "Air Astana", "category": "Авиация / Транспорт", "website": "airastana.com", "contact_name": "Питер Фостер", "contact_position": "CEO", "contact_linkedin": "linkedin.com/company/air-astana", "contact_email": "info@airastana.com", "priority": "high", "use_case": "Бортовые объявления и голосовой ассистент на казахском"},
    {"company_name": "FlyArystan", "category": "Авиация / Транспорт", "website": "flyarystan.com", "contact_email": "info@flyarystan.com", "contact_linkedin": "linkedin.com/company/flyarystan", "priority": "medium", "use_case": "Казахскоязычные объявления и IVR"},
    # CRM/ERP
    {"company_name": "1C Казахстан", "category": "CRM / ERP", "website": "1c.kz", "contact_email": "info@1c.kz", "contact_phone": "+7 727 355 24 00", "contact_linkedin": "linkedin.com/company/1c-kazakhstan", "priority": "high", "use_case": "Голосовые модули для продуктов 1С на казахском"},
    {"company_name": "Битрикс24 KZ (партнёры)", "category": "CRM / ERP", "website": "bitrix24.kz", "contact_email": "info@bitrix24.kz", "contact_linkedin": "linkedin.com/company/bitrix24", "priority": "high", "use_case": "Интеграция TTS/STT в Битрикс24 для казахстанских клиентов"},
    # Call Centers
    {"company_name": "Prime Source", "category": "Колл-центры", "website": "primesource.kz", "contact_email": "info@primesource.kz", "contact_linkedin": "linkedin.com/company/prime-source-kz", "priority": "medium", "use_case": "STT-аналитика звонков и голосовые боты на казахском"},
    # Media
    {"company_name": "Ours.kz / Kolesa Group", "category": "Медиа", "website": "kolesa.kz", "contact_linkedin": "linkedin.com/company/kolesa-kz", "priority": "low", "use_case": "Озвучка контента на казахском"},
    {"company_name": "Tengri Media", "category": "Медиа", "website": "tengrinews.kz", "contact_email": "info@tengrinews.kz", "contact_linkedin": "linkedin.com/company/tengrinews", "priority": "medium", "use_case": "Аудиоверсии новостей на казахском TTS"},
]

DATASET_PARTNERS = [
    # TV
    {"company_name": "Қазақстан (Qazaqstan TV)", "category": "Телевидение", "website": "tv.kz", "contact_name": "Дирекция по производству", "contact_email": "info@tv.kz", "contact_phone": "+7 727 272 90 10", "contact_linkedin": "linkedin.com/company/qazaqstan-tv", "priority": "high", "dataset_types": "audio,video", "dataset_language": "kz", "collaboration_type": "partnership", "use_case": "Архивные казахскоязычные передачи и новости для обучения TTS/STT"},
    {"company_name": "Хабар (Khabar Agency)", "category": "Телевидение", "website": "khabar.kz", "contact_email": "info@khabar.kz", "contact_phone": "+7 727 258 08 00", "contact_linkedin": "linkedin.com/company/khabar-agency", "priority": "high", "dataset_types": "audio,video,text", "dataset_language": "kz,ru", "collaboration_type": "partnership", "use_case": "Видео- и аудиоархив на казахском и русском"},
    {"company_name": "Балапан TV", "category": "Телевидение", "website": "balapan.kz", "contact_email": "info@balapan.kz", "priority": "high", "dataset_types": "audio,video", "dataset_language": "kz", "collaboration_type": "partnership", "use_case": "Детский казахский контент — чистая речь, идеальна для TTS"},
    {"company_name": "31 канал", "category": "Телевидение", "website": "31.kz", "contact_email": "info@31.kz", "contact_phone": "+7 727 258 31 31", "priority": "medium", "dataset_types": "audio,video", "dataset_language": "kz,ru", "collaboration_type": "partnership", "use_case": "Казахскоязычный развлекательный контент"},
    {"company_name": "QAZAQ TV", "category": "Телевидение", "website": "qazaqtv.com", "contact_email": "info@qazaqtv.com", "priority": "high", "dataset_types": "audio,video", "dataset_language": "kz", "collaboration_type": "partnership", "use_case": "Международное вещание на казахском языке"},
    # Radio
    {"company_name": "Қазақ Радиосы", "category": "Радио", "website": "qazradio.fm", "contact_email": "info@qazradio.fm", "contact_phone": "+7 727 272 99 10", "priority": "high", "dataset_types": "audio", "dataset_language": "kz", "collaboration_type": "partnership", "use_case": "Архив радиопередач на казахском — эталонная речь дикторов"},
    {"company_name": "Hit FM Казахстан", "category": "Радио", "website": "hitfm.kz", "contact_email": "info@hitfm.kz", "contact_linkedin": "linkedin.com/company/hit-fm-kazakhstan", "priority": "medium", "dataset_types": "audio", "dataset_language": "ru,kz", "collaboration_type": "partnership", "use_case": "Аудио ведущих и джинглов"},
    {"company_name": "Tengri FM", "category": "Радио", "website": "tengrifm.kz", "contact_email": "info@tengrifm.kz", "priority": "medium", "dataset_types": "audio", "dataset_language": "kz,ru", "collaboration_type": "partnership", "use_case": "Архив радиопередач"},
    {"company_name": "Ретро FM Казахстан", "category": "Радио", "website": "retro.kz", "contact_email": "info@retro.kz", "priority": "low", "dataset_types": "audio", "dataset_language": "ru", "collaboration_type": "partnership", "use_case": "Русскоязычный аудиоархив"},
    # Publishing
    {"company_name": "Атамұра", "category": "Издательства", "website": "atamura.kz", "contact_email": "info@atamura.kz", "contact_phone": "+7 727 391 83 83", "contact_linkedin": "linkedin.com/company/atamura", "priority": "high", "dataset_types": "text", "dataset_language": "kz", "collaboration_type": "partnership", "use_case": "Учебники и литература на казахском — эталонный литературный язык"},
    {"company_name": "Мектеп", "category": "Издательства", "website": "mektep.kz", "contact_email": "info@mektep.kz", "priority": "high", "dataset_types": "text", "dataset_language": "kz,ru", "collaboration_type": "partnership", "use_case": "Школьные учебники на казахском — нормированный текст"},
    {"company_name": "Фолиант", "category": "Издательства", "website": "foliant.kz", "contact_email": "info@foliant.kz", "priority": "medium", "dataset_types": "text", "dataset_language": "kz,ru", "collaboration_type": "paid", "use_case": "Казахская художественная литература"},
    # Universities
    {"company_name": "КазНУ им. аль-Фараби", "category": "Университеты", "website": "kaznu.kz", "contact_email": "info@kaznu.kz", "contact_phone": "+7 727 377 33 33", "contact_linkedin": "linkedin.com/school/al-farabi-kazakh-national-university", "priority": "high", "dataset_types": "text,audio", "dataset_language": "kz,ru", "collaboration_type": "partnership", "use_case": "Академические корпуса казахского языка и речевые базы"},
    {"company_name": "Назарбаев Университет", "category": "Университеты", "website": "nu.edu.kz", "contact_email": "info@nu.edu.kz", "contact_linkedin": "linkedin.com/school/nazarbayev-university", "priority": "high", "dataset_types": "text", "dataset_language": "kz,ru,en", "collaboration_type": "partnership", "use_case": "Исследовательское партнёрство по NLP и TTS"},
    {"company_name": "ЕНУ им. Гумилёва", "category": "Университеты", "website": "enu.kz", "contact_email": "info@enu.kz", "contact_phone": "+7 7172 709 500", "contact_linkedin": "linkedin.com/school/eurasian-national-university", "priority": "medium", "dataset_types": "text,audio", "dataset_language": "kz,ru", "collaboration_type": "partnership", "use_case": "Казахский языковой корпус и лингвистические данные"},
    {"company_name": "КазПедУ (Абай)", "category": "Университеты", "website": "kaznpu.kz", "contact_email": "info@kaznpu.kz", "priority": "medium", "dataset_types": "text,audio", "dataset_language": "kz", "collaboration_type": "partnership", "use_case": "Педагогические материалы и речевые корпуса"},
    # Libraries
    {"company_name": "Нац. библиотека РК", "category": "Библиотеки", "website": "nlrk.kz", "contact_email": "info@nlrk.kz", "contact_phone": "+7 727 272 06 36", "priority": "high", "dataset_types": "text", "dataset_language": "kz,ru", "collaboration_type": "partnership", "use_case": "Оцифрованные фонды казахских книг и рукописей"},
    {"company_name": "Президентская библиотека РК", "category": "Библиотеки", "website": "preslib.kz", "contact_email": "info@preslib.kz", "priority": "medium", "dataset_types": "text", "dataset_language": "kz,ru", "collaboration_type": "partnership", "use_case": "Архивные казахские тексты для обучения языковых моделей"},
    # Film
    {"company_name": "Казахфильм", "category": "Кино / Студии", "website": "kazakhfilm.kz", "contact_email": "info@kazakhfilm.kz", "contact_phone": "+7 727 399 18 00", "contact_linkedin": "linkedin.com/company/kazakhfilm", "priority": "high", "dataset_types": "audio,video", "dataset_language": "kz,ru", "collaboration_type": "partnership", "use_case": "Аудиодорожки казахских фильмов — богатый разговорный корпус"},
    # Newspapers
    {"company_name": "Egemen Qazaqstan", "category": "Газеты / СМИ", "website": "egemen.kz", "contact_email": "info@egemen.kz", "contact_phone": "+7 727 272 36 49", "priority": "high", "dataset_types": "text", "dataset_language": "kz", "collaboration_type": "partnership", "use_case": "Архив старейшей казахской газеты — большой текстовый корпус"},
    {"company_name": "Казинформ", "category": "Газеты / СМИ", "website": "inform.kz", "contact_email": "kazinform@inform.kz", "contact_phone": "+7 7172 720 070", "contact_linkedin": "linkedin.com/company/kazinform", "priority": "high", "dataset_types": "text", "dataset_language": "kz,ru,en", "collaboration_type": "partnership", "use_case": "Новостной корпус на трёх языках — трёхъязычные параллельные тексты"},
    {"company_name": "Казахстанская правда", "category": "Газеты / СМИ", "website": "kazpravda.kz", "contact_email": "info@kazpravda.kz", "priority": "medium", "dataset_types": "text", "dataset_language": "ru", "collaboration_type": "partnership", "use_case": "Большой архив русскоязычного казахстанского текста"},
    # Music
    {"company_name": "Asyl Music", "category": "Музыка", "website": "asylmusic.kz", "contact_email": "info@asylmusic.kz", "contact_telegram": "@asylmusic", "priority": "medium", "dataset_types": "audio", "dataset_language": "kz", "collaboration_type": "paid", "use_case": "Казахские песни с текстами для обучения интонации"},
    # Language institutes
    {"company_name": "Институт языкознания им. А. Байтурсынова", "category": "Языковые институты", "website": "ilin.kz", "contact_email": "ilin@inbox.ru", "contact_phone": "+7 727 272 04 83", "priority": "high", "dataset_types": "text,audio", "dataset_language": "kz", "collaboration_type": "partnership", "use_case": "Нормативные словари, фонетические базы, лингвистические корпуса казахского"},
    {"company_name": "Терминологический комитет МКП РК", "category": "Языковые институты", "website": "mks.gov.kz", "contact_email": "info@mks.gov.kz", "priority": "high", "dataset_types": "text", "dataset_language": "kz", "collaboration_type": "partnership", "use_case": "Официальная терминология и нормы казахского языка для TTS"},
]


def get_all_seed_data():
    result = []
    for p in B2B_PARTNERS:
        msg = generate_message(
            p["company_name"],
            p["category"],
            p.get("contact_name"),
            p.get("use_case", ""),
        )
        result.append({**p, "partner_type": "b2b", "status": "new", "generated_message": msg})

    for p in DATASET_PARTNERS:
        msg = generate_message(
            p["company_name"],
            p["category"],
            p.get("contact_name"),
            p.get("use_case", ""),
        )
        result.append({**p, "partner_type": "dataset", "status": "new", "generated_message": msg})

    return result
