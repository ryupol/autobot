# Cookie Run — Strategy Guides

Collection of builds, clear times, and tips for each strategy.

---

## FarmBox (idle)

No key presses during the run — the script just waits for the stage to finish
while your selected team auto-clears it.

Pass your clear time with `--time` (in minutes). A random 0–10% jitter is
added automatically so the wait isn't identical every round:

```powershell
python -m gamebots.games.cookie_run box --time 3.6
```

If omitted, the default is `FARM_BOX_DEFAULT_DURATION` in `strategy_config.py`.

### Reference builds

| Build                                               | Clear time       | Command                                               |
| --------------------------------------------------- | ---------------- | ----------------------------------------------------- |
| [754](https://www.cookierunhub.com/en/episodes/754) | ~3:31 (3.52 min) | `python -m gamebots.games.cookie_run box --time 3.52` |
| [740](https://www.cookierunhub.com/en/episodes/740) | ~1:40 (1.67 min) | `python -m gamebots.games.cookie_run box --time 1.67` |
| [790](https://www.cookierunhub.com/en/episodes/790) | ~2:35 (2.59 min) | `python -m gamebots.games.cookie_run box --time 2.59` |
| [299](https://www.cookierunhub.com/en/episodes/299) | ~3:36 (3.59 min) | `python -m gamebots.games.cookie_run box --time 3.59` |

Adjust the value up or down if your build is faster or slower.
