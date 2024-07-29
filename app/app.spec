# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('api.py', '.'),
        ('brands.py', '.'),
        ('page.py', '.'),
        ('constants.py', '.'),
        ('parsers_data.py', '.'),
        ('../.env', '.'),
        ('templates', 'templates'),
        ('static', 'static')
    ],
    hiddenimports=[
        'aiohttp',
        'asyncio',
        'os',
        'multiprocessing',
        'fastapi',
        'fastapi.responses',
        'fastapi.staticfiles',
        'fastapi.templating',
        'dotenv',
        'zeep',
        'uvicorn',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon_auto.ico'],
)