# Cookie Run Classic

[ภาษาไทย](#ภาษาไทย) | [English](#english)

![Cookie Run script button positions](images/button_position.png)

## ภาษาไทย

สคริปต์ Cookie Run Classic ช่วยเล่นด่าน เก็บรางวัล และเริ่มรอบใหม่อัตโนมัติ
ต้องเริ่มจากหน้า Home ของ Episode ใดก็ได้

ปุ่มที่สคริปต์คาดไว้แสดงอยู่ในภาพด้านบน โดยมีรายละเอียดดังนี้:

- `D`: เริ่มเกมและสไลด์
- `A` หรือ `Space`: กระโดด
- `1`, `2`: เลือกเมนู ไอเทม และรับรางวัล
- `V`, `W`, `Z`, `B`: นำทางเมนูและเลือกโหมดการเล่น
- `P`: เปิดเมนู Pet
- `S`: ยืนยันหรือเลือกปุ่มในบางหน้าจอ
- `O`: ยืนยันการจบรอบ
- `Q`: ออกจากหน้าปัจจุบัน
- `Esc`: เปิดเมนูหยุดชั่วคราวหรือย้อนกลับ

ต้องตั้งค่าปุ่มในเกมหรือ emulator ให้ตรงกับรายการนี้ก่อนเริ่มสคริปต์

### ก่อนเริ่ม

1. เปิด Episode ใดก็ได้
2. อยู่ที่หน้า Home ของ Episode
3. ตรวจสอบว่าตั้งค่าปุ่มตรงกับสคริปต์
4. เปิด terminal ที่ root ของโปรเจกต์
5. รัน strategy ที่ต้องการ
6. ระหว่างนับถอยหลัง 3 วินาที ให้สลับกลับไปหน้าเกม

Strategy มาตรฐานจะเข้าหน้าเตรียมเกม เลือก Double Coin เริ่มวิ่ง เล่นด่าน
เก็บรางวัล และเริ่มรอบใหม่อัตโนมัติ ค่าเริ่มต้นรัน 100 รอบ
และมีพักเป็นครั้งคราว

เปลี่ยนจำนวนรอบได้ด้วย `--rounds`:

```powershell
python -m gamebots.games.cookie_run 2 --rounds 10
```

### Strategy 1 — กระโดดสองชั้นอัตโนมัติ

```powershell
python -m gamebots.games.cookie_run 1
```

วนรอบอัตโนมัติ ใช้รูปแบบเน้นกระโดดสองชั้น และสุ่มเวลาด้วย Gaussian timing

### Strategy 2 — กระโดดสองชั้นอัตโนมัติ

```powershell
python -m gamebots.games.cookie_run 2
```

วนรอบอัตโนมัติ เน้นกระโดดสองชั้น และมีการกระโดดครั้งเดียว สไลด์
หรือแก้จังหวะเป็นครั้งคราว

### Strategy 3 — กระโดดครั้งเดียวอัตโนมัติ

```powershell
python -m gamebots.games.cookie_run 3
```

วนรอบอัตโนมัติ เน้นกระโดดครั้งเดียว และรอช่วงสั้นก่อนเริ่มกดปุ่มระหว่างวิ่ง

### สุ่ม Strategy 1–3

```powershell
python -m gamebots.games.cookie_run mixed
```

สุ่มใช้ Strategy 1, 2 หรือ 3 ใหม่ในแต่ละรอบ

### Strategy 4 — โหมด external hotkey

```powershell
python -m gamebots.games.cookie_run 4
```

โหมดทดลอง หลังเตรียมเกมจะกด `Right Alt` ร่วมกับปุ่มสุ่ม `0`, `-` หรือ `=`
แล้วรอจนจบรอบ ใช้เฉพาะเมื่อตั้งค่า emulator หรือ external hotkey
สำหรับปุ่มเหล่านี้แล้ว

### การตั้งค่า Strategy

ค่าที่แก้ไขได้ของแต่ละ FarmCoin อยู่ในไฟล์
`gamebots/games/cookie_run/strategy_config.py` เพื่อให้ปรับเวลาและพฤติกรรมได้ง่าย
โดยไม่ต้องแก้ logic ใน `strategies.py`:

- `*_DURATION_RANGE`: ช่วงเวลาที่ฟาร์ม หน่วยเป็นนาที
- `*_INITIAL_WAIT_RANGE`: เวลารอก่อนเริ่ม หน่วยเป็นวินาที หรือ `None` ถ้าไม่ต้องการรอ
- `*_PATTERN_WEIGHTS`: น้ำหนักโอกาสของรูปแบบการเคลื่อนไหว ตัวเลขมากจะมีโอกาสมากขึ้น
- `*_REWARD_PRESS_RANGE`: จำนวนครั้งที่กดหน้าเก็บรางวัล
- `*_REWARD_WAIT_RANGE`: ช่วงเวลาระหว่างการกดเก็บรางวัล หน่วยเป็นวินาที
- `PATTERN_BREAK_CHANCE`: โอกาสที่จะหยุดพักหลังเล่นแต่ละ pattern เช่น `0.002` = 0.2%
- `PATTERN_BREAK_RANGE`: ช่วงเวลาของการหยุดพัก หน่วยเป็นวินาที

ลำดับของ `PATTERN_WEIGHTS` สำหรับ Strategy 1, 2 และ 3 คือ `single_jump`,
`double_jump`, `short_slide`, `long_slide`, `panic`

ช่วงเวลาการเก็บรางวัลจะถูกสุ่มให้คลาดเคลื่อนเล็กน้อยในแต่ละ instance
เพื่อไม่ให้จังหวะการกดเหมือนเดิมทุกครั้ง

### แก้ปัญหา

- เริ่มจากเมนูผิด: กลับหน้า Home ของ Episode แล้วเริ่ม script ใหม่
- เลือกไอเทมไม่ถูก: ตรวจสอบปุ่มตัวเลขและ focus ของเกม
- จังหวะกระโดดไม่ตรง: ลอง Strategy อื่นหรือปรับเวลาในโค้ด
- Emulator หยุดผิดจังหวะ: ตรวจสอบปุ่ม `Esc`, `O` และ `Q`
- หยุดสคริปต์: กลับไป terminal แล้วกด `Ctrl+C`

### เพิ่ม Strategy ใหม่ (เช่น 5, 6)

1. สร้างคลาสใหม่ใน `strategies.py` สืบทอดจาก `FarmCoinBase`
   (หรือ `PatternFarmCoin`) แล้ว implement เมท็อด `run()`
2. export คลาสใน `__init__.py`
3. เพิ่มลง dict `STRATEGIES` ใน `__main__.py`:

   ```python
   STRATEGIES = {
       "1": FarmCoin1,
       # ...
       "5": FarmCoin5,   # เพิ่มบรรทัดนี้
   }
   ```

   เท่านี้ก็รันด้วย `python -m gamebots.games.cookie_run 5` ได้

**เพิ่มลงโหมด `mixed`:** แก้ค่า default `farm_classes` ใน `run_mixed`
ที่ `runner.py`:

```python
def run_mixed(rounds=100, farm_classes=(FarmCoin1, FarmCoin2, FarmCoin3)):
```

เพิ่มคลาสที่ต้องการลงใน tuple เช่น `(FarmCoin1, FarmCoin2, FarmCoin3, FarmCoin5)`
Strategy ที่อยู่ใน `STRATEGIES` แต่ไม่อยู่ใน tuple นี้ จะรันได้เฉพาะแบบระบุตรง ๆ
เท่านั้น (ไม่ถูกสุ่มใน `mixed`) — เช่นเดียวกับ `FarmCoin4` ตอนนี้

---

## English

Cookie Run Classic scripts automate episode runs, reward collection, and repeated
rounds. Start from home page of any episode.

The expected script buttons are shown in the image above:

- `D`: start the run and slide;
- `A` or `Space`: jump;
- `1`, `2`: menu, item, and reward selection;
- `V`, `W`, `Z`, `B`: menu navigation and game-mode selection;
- `P`: open the Pet menu;
- `S`: confirm or select on certain screens;
- `O`: confirm the end-of-round flow;
- `Q`: exit the current screen;
- `Esc`: open the pause menu or go back.

Configure the game or emulator controls to match these keys before starting
the script.

## Before starting

1. Open any episode.
2. Stay on episode home page.
3. Confirm expected keyboard bindings.
4. Open terminal in project root.
5. Run selected strategy.
6. Switch focus to game during 3-second countdown.

Each standard strategy automatically opens preparation, selects Double Coin,
starts run, plays, collects rewards, and loops. Default runner performs 100
rounds with occasional breaks.

Change round count with `--rounds`:

```powershell
python -m gamebots.games.cookie_run 2 --rounds 10
```

## Strategy 1 — automatic double jump

```powershell
python -m gamebots.games.cookie_run 1
```

Uses automatic loop with double-jump-oriented sequence and Gaussian timing.

## Strategy 2 — automatic double jump

```powershell
python -m gamebots.games.cookie_run 2
```

Uses automatic loop with double jump as primary pattern plus occasional single
jump, slide, and recovery patterns.

## Strategy 3 — automatic single jump

```powershell
python -m gamebots.games.cookie_run 3
```

Uses automatic loop with single jump as primary pattern. Adds initial wait
before gameplay actions.

## Mixed strategies 1–3

```powershell
python -m gamebots.games.cookie_run mixed
```

Randomly selects strategy 1, 2, or 3 for each round.

## Strategy 4 — external hotkey mode

```powershell
python -m gamebots.games.cookie_run 4
```

Experimental mode. After preparation, presses `Right Alt` with random
`0`, `-`, or `=` key, then waits for run duration. Use only when emulator or
external hotkeys are configured for this behavior.

## Strategy configuration

Editable settings for each FarmCoin are in
`gamebots/games/cookie_run/strategy_config.py`. This lets you tune timing and
behavior without changing the automation logic in `strategies.py`:

- `*_DURATION_RANGE`: farming duration in minutes.
- `*_INITIAL_WAIT_RANGE`: wait before starting, in seconds, or `None` for no wait.
- `*_PATTERN_WEIGHTS`: relative probability of each movement pattern; larger
  numbers are more likely.
- `*_REWARD_PRESS_RANGE`: number of reward-screen taps.
- `*_REWARD_WAIT_RANGE`: delay range between reward-screen taps, in seconds.
- `PATTERN_BREAK_CHANCE`: chance of taking a break after each pattern; `0.002` = 0.2%.
- `PATTERN_BREAK_RANGE`: break duration range, in seconds.

For Strategies 1, 2, and 3, `PATTERN_WEIGHTS` order is `single_jump`,
`double_jump`, `short_slide`, `long_slide`, `panic`.

Reward-screen timing ranges receive a very small random variation for each
instance, so the cadence is not identical every time.

## Troubleshooting

- Script starts from wrong menu: return to episode home page and restart.
- Item selection fails: verify number-key mappings and game focus.
- Jump timing fails: choose another strategy or adjust timing code.
- Emulator pauses unexpectedly: confirm `Esc`, `O`, and `Q` mappings.
- Stop automation: focus terminal and press `Ctrl+C`.

## Adding a new strategy (e.g. 5, 6)

1. Create a new class in `strategies.py` subclassing `FarmCoinBase`
   (or `PatternFarmCoin`) and implement `run()`.
2. Export the class in `__init__.py`.
3. Register it in the `STRATEGIES` dict in `__main__.py`:

   ```python
   STRATEGIES = {
       "1": FarmCoin1,
       # ...
       "5": FarmCoin5,   # add this line
   }
   ```

   It is now runnable with `python -m gamebots.games.cookie_run 5`.

**Include it in `mixed`:** edit the default `farm_classes` in `run_mixed`
in `runner.py`:

```python
def run_mixed(rounds=100, farm_classes=(FarmCoin1, FarmCoin2, FarmCoin3)):
```

Add the class to the tuple, e.g. `(FarmCoin1, FarmCoin2, FarmCoin3, FarmCoin5)`.
A strategy registered in `STRATEGIES` but left out of this tuple is only
runnable when named explicitly (never picked by `mixed`) — this is exactly how
`FarmCoin4` behaves today.
