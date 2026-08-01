# Gamebots

[ภาษาไทย](#ภาษาไทย) | [English](#english)

## ภาษาไทย

Gamebots คือชุดสคริปต์กดคีย์บอร์ดอัตโนมัติตามเวลาสำหรับ:

- Monster Hunter: World
- Clair Obscur: Expedition 33
- Cookie Run Classic

โค้ดรับอินพุตของ Windows ที่ใช้ร่วมกันอยู่ใน `gamebots/core/`
ส่วน component, strategy และ runner ของแต่ละเกมอยู่ใน `gamebots/games/`

สคริปต์ส่งคีย์บอร์ดตรงไปยังหน้าต่างที่กำลัง active โดยไม่ตรวจจับภาพหน้าจอ
ดังนั้นตำแหน่งเริ่มต้น ปุ่มควบคุม และเวลาโหลดต้องตรงกับที่สคริปต์คาดไว้

### README แต่ละเกม

- [Monster Hunter: World](gamebots/games/monster_hunter_world/README.md#ภาษาไทย)
- [Clair Obscur: Expedition 33](gamebots/games/expedition_33/README.md#ภาษาไทย)
- [Cookie Run Classic](gamebots/games/cookie_run/README.md#ภาษาไทย) — ดู
  [GUIDES.md](gamebots/games/cookie_run/GUIDES.md) สำหรับตัวอย่างบิวด์และเวลา

> **แนะนำ:** สำหรับ Cookie Run Classic ให้ใช้โหมด `box`
> (`python -m gamebots.games.cookie_run box`) เพราะจากที่ลองใช้มา ยังไม่เจอ
> CAPTCHA ขึ้นระหว่างรัน ส่วนโหมด/เกมอื่นเจอ CAPTCHA ได้ ควรเฝ้าดูใกล้ ๆ
> เมื่อใช้งาน แนะนำให้เล่นผ่าน emulator **LDPlayer 14**
> (<https://www.ldplayer.net/>)

> **สำคัญ:** สคริปต์นี้เป็นตัวจำลองการกดคีย์บอร์ด (keyboard press simulator)
> ไม่ใช่การควบคุมเกมโดยตรง ต้องเปิดหน้าต่างเกมเป้าหมายไว้เป็นหน้าต่างที่ active
> (focus) ตลอดการทำงาน ห้ามสลับไปแอปอื่นระหว่างรัน เพราะปุ่มที่กดจะไปกดที่
> หน้าต่างอื่นแทน

### ความต้องการของระบบ

- Windows 10 หรือ 11
- Python 3.10 ขึ้นไป
- เกมตั้งค่าปุ่มตามที่สคริปต์คาดไว้
- PowerShell หรือ Command Prompt

ไม่ต้องติดตั้ง Python package เพิ่ม

### การติดตั้ง

1. ติดตั้ง Python จาก <https://www.python.org/downloads/>
2. ระหว่างติดตั้ง เลือก **Add Python to PATH**
3. ดาวน์โหลดหรือ clone repository นี้
4. เปิด PowerShell ในโฟลเดอร์โปรเจกต์
5. ตรวจสอบ Python:

```powershell
python --version
```

ถ้าไม่มีคำสั่ง `python` ให้ใช้ Python Launcher:

```powershell
py --version
```

### การรัน

เตรียมเกมตาม README ของเกมนั้น แล้วรันคำสั่ง:

| เกม/โหมด | คำสั่ง | วิธีใช้ |
|---|---|---|
| MHW ฟาร์ม Icebloom | `python -m gamebots.games.monster_hunter_world icebloom` | [README MHW](gamebots/games/monster_hunter_world/README.md#ภาษาไทย) |
| MHW Tailraider | `python -m gamebots.games.monster_hunter_world tailraider` | [README MHW](gamebots/games/monster_hunter_world/README.md#ภาษาไทย) |
| Expedition 33 ฟาร์ม EXP | `python -m gamebots.games.expedition_33` | [README Expedition 33](gamebots/games/expedition_33/README.md#ภาษาไทย) |
| Cookie Run Classic โหมด `box` (แนะนำ) | `python -m gamebots.games.cookie_run box --time 3.6` | [README Cookie Run Classic](gamebots/games/cookie_run/README.md#ภาษาไทย) |
| Cookie Run Classic สุ่มแบบ 1–3 | `python -m gamebots.games.cookie_run mixed` | [README Cookie Run Classic](gamebots/games/cookie_run/README.md#ภาษาไทย) |

ดูแบบ (strategy) อื่นของ Cookie Run Classic ทั้งหมดได้ที่
[README Cookie Run Classic](gamebots/games/cookie_run/README.md#ภาษาไทย)

เปลี่ยน `python` เป็น `py` ได้เมื่อจำเป็น:

```powershell
py -m gamebots.games.monster_hunter_world icebloom
```

แต่ละ launcher นับถอยหลัง 3–5 วินาทีสำหรับสลับกลับไปหน้าเกม (ดูจำนวนวินาที
ที่แน่นอนได้ใน README ของเกมนั้น)
หยุดสคริปต์ได้ด้วย `Ctrl+C` ใน terminal

`-m` ย่อมาจาก module ให้ Python หา package ตาม import path แล้วรันไฟล์
`__main__.py` ของ package นั้น ตัวอย่าง:

```powershell
python -m gamebots.games.cookie_run 2
```

คำสั่งนี้รัน `gamebots/games/cookie_run/__main__.py` และส่ง `2`
เข้าไปเป็น strategy

### โครงสร้างโปรเจกต์

```text
gamebots/
├── core/
│   ├── action.py
│   └── windows_input.py
└── games/
    ├── cookie_run/
    ├── expedition_33/
    └── monster_hunter_world/
```

แต่ละเกมมี `__main__.py` เป็น command-line entry point และมี logic อยู่ใน
package ของเกมนั้น ไม่มี compatibility launcher เก่าที่ root แล้ว

### การทดสอบ

Test ใช้ input ปลอมและจะไม่กดปุ่มจริง:

```powershell
python -m unittest discover -v
```

### ข้อควรระวัง

ควรเฝ้าดูอย่างน้อยหนึ่งรอบเต็มก่อนปล่อยให้ทำงานเอง เวลาอาจคลาดเคลื่อนเมื่อเกม
กระตุก โหลดช้า หน้าต่างเกมไม่ได้ active หรือปุ่มควบคุมไม่ตรง
ตรวจสอบกฎและเงื่อนไขของแต่ละเกมก่อนใช้ระบบอัตโนมัติ


---

## English

Gamebots is a collection of timed keyboard automation scripts for:

- Monster Hunter: World;
- Clair Obscur: Expedition 33;
- Cookie Run Classic.

Shared Windows input code lives in `gamebots/core/`. Each game has isolated
components, strategies, and runners under `gamebots/games/`.

These scripts send keyboard input directly to the focused window. They do not
use screen recognition, so correct starting position, key bindings, and loading
times matter.

### Per-game READMEs

- [Monster Hunter: World](gamebots/games/monster_hunter_world/README.md)
- [Clair Obscur: Expedition 33](gamebots/games/expedition_33/README.md)
- [Cookie Run Classic](gamebots/games/cookie_run/README.md) — see
  [GUIDES.md](gamebots/games/cookie_run/GUIDES.md) for reference builds and
  clear times

> **Recommended:** for Cookie Run Classic, use `box` mode
> (`python -m gamebots.games.cookie_run box`). In testing so far it has not
> triggered a CAPTCHA, while other modes/games can. Watch closely when using
> any mode. Recommended emulator: **LDPlayer 14** (<https://www.ldplayer.net/>).

> **Important:** this project is a keyboard press simulator, not direct game
> control. Keep the target game window focused (active) for the entire run.
> Do not switch to another app while a script is running — key presses will
> go to whatever window is focused instead.

## Requirements

- Windows 10 or 11;
- Python 3.10 or newer;
- game using expected keyboard bindings;
- terminal such as PowerShell or Command Prompt.

No third-party Python packages are required.

## Install

1. Install Python from <https://www.python.org/downloads/>.
2. During installation, enable **Add Python to PATH**.
3. Download or clone this repository.
4. Open PowerShell in project folder.
5. Check Python:

```powershell
python --version
```

If `python` is unavailable, use Windows launcher:

```powershell
py --version
```

## Run

Prepare game using its game-specific README, then launch matching script:

| Game/mode | Command | Instructions |
|---|---|---|
| MHW Icebloom | `python -m gamebots.games.monster_hunter_world icebloom` | [MHW README](gamebots/games/monster_hunter_world/README.md) |
| MHW Tailraider | `python -m gamebots.games.monster_hunter_world tailraider` | [MHW README](gamebots/games/monster_hunter_world/README.md) |
| Expedition 33 EXP farm | `python -m gamebots.games.expedition_33` | [Expedition 33 README](gamebots/games/expedition_33/README.md) |
| Cookie Run Classic `box` mode (recommended) | `python -m gamebots.games.cookie_run box --time 3.6` | [Cookie Run Classic README](gamebots/games/cookie_run/README.md) |
| Cookie Run Classic mixed 1–3 | `python -m gamebots.games.cookie_run mixed` | [Cookie Run Classic README](gamebots/games/cookie_run/README.md) |

See [Cookie Run Classic README](gamebots/games/cookie_run/README.md) for all
other Cookie Run Classic strategies.

Replace `python` with `py` when needed:

```powershell
py -m gamebots.games.monster_hunter_world icebloom
```

Each launcher gives 3–5 seconds to focus game window (see each game's README
for the exact duration). Stop automation from terminal with `Ctrl+C`.

`-m` means module. Python resolves the package through its import path, then
runs that package’s `__main__.py`. For example:

```powershell
python -m gamebots.games.cookie_run 2
```

This runs `gamebots/games/cookie_run/__main__.py` and passes `2` as the
strategy.

## Project structure

```text
gamebots/
├── core/
│   ├── action.py
│   └── windows_input.py
└── games/
    ├── cookie_run/
    ├── expedition_33/
    └── monster_hunter_world/
```

Each game contains a `__main__.py` command-line entry point and keeps its
behavior inside its package. Old root compatibility launchers are removed.

## Tests

Tests use fake input and do not press real keys:

```powershell
python -m unittest discover -v
```

## Important

Watch first complete loop before leaving automation unattended. Timing can drift
when game lags, loading takes longer, window focus changes, or key bindings
differ. Check each game’s rules and terms before using automation.
