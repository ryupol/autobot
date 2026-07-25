# Clair Obscur: Expedition 33

[ภาษาไทย](#ภาษาไทย) | [English](#english)

## ภาษาไทย

สคริปต์นี้ฟาร์ม EXP โดยต่อสู้กับ merchant ที่ Renoir’s Draft ซ้ำ

วิดีโออ้างอิง: <https://www.youtube.com/watch?v=_SijRHlymo4>

### สิ่งที่ต้องเตรียม

1. Maelle ต้องฆ่าศัตรูทั้งหมดได้ด้วย Phantom Strike หนึ่งครั้ง
2. ใส่ Phantom Strike ไว้ช่อง `E` ซึ่งเป็นช่องล่างสุดทางซ้าย
3. ต่อสู้กับ merchant ด้วยตัวเองหนึ่งรอบ
4. หลังจบการต่อสู้ กด `F` ที่ **We Continue** หนึ่งครั้ง
5. หยุดรอที่หน้าบทสนทนาของ merchant

สคริปต์ใช้ปุ่มควบคุมเริ่มต้นและต้องเริ่มจากหน้าบทสนทนาที่ถูกต้อง

### การรัน

รันจาก root ของโปรเจกต์:

```powershell
python -m gamebots.games.expedition_33
```

ระหว่างนับถอยหลัง 3 วินาที ให้สลับกลับไปหน้าเกม จากนั้นสคริปต์จะ:

1. กดผ่านบทสนทนา
2. เริ่มการต่อสู้
3. เลือก skill ที่ตั้งไว้
4. ใช้ลำดับปุ่มโจมตี
5. กลับไปหน้าบทสนทนา
6. ทำซ้ำ

ค่าเริ่มต้นรัน 100 รอบ

เปลี่ยนจำนวนรอบ:

```powershell
python -m gamebots.games.expedition_33 --rounds 10
```

### แก้ปัญหา

- เลือกเมนูผิด: คืนค่าปุ่มควบคุมและกลับไปหน้าบทสนทนาเริ่มต้น
- Skill ฆ่าไม่หมด: ปรับ build ของ Maelle ก่อนลองใหม่
- Sequence คลาดเคลื่อน: ตรวจสอบว่าเกม active และเครื่องทำงานเสถียร
- หยุดฉุกเฉิน: กลับไป terminal แล้วกด `Ctrl+C`


---

## English

This script farms EXP by repeatedly fighting merchant in Renoir’s Draft.

Reference route: <https://www.youtube.com/watch?v=_SijRHlymo4>

## Prerequisites

1. Maelle must defeat all enemies with one use of Phantom Strike.
2. Put Phantom Strike in `E` slot, lowest slot on left side.
3. Manually fight merchant once.
4. After fight, press `F` for **We Continue** once.
5. Stop at merchant dialog screen.

Script expects default keyboard controls and exact dialog state.

## Run

From project root:

```powershell
python -m gamebots.games.expedition_33
```

During 3-second countdown, focus game window. Script then:

1. advances merchant dialog;
2. starts fight;
3. selects configured skill;
4. executes attack sequence;
5. returns to dialog;
6. repeats.

Default runner performs 100 rounds.

Change round count:

```powershell
python -m gamebots.games.expedition_33 --rounds 10
```

## Troubleshooting

- Wrong menu option: restore default key bindings and starting dialog.
- Skill misses/fails to kill: improve Maelle setup before retrying.
- Sequence drifts: verify game is focused and performance is stable.
- Need emergency stop: focus terminal and press `Ctrl+C`.
