# ba_meta require api 8
import bs
import bsSpaz

# ba_meta export bs.Plugin
class KillerPunchPlugin(bs.Plugin):
    def __init__(self):
        bs.screenMessage("🔥 KillerPunchPlugin فعال شد! 👊")

        self._original_punch = bsSpaz.Spaz.onPunched
        bsSpaz.Spaz.onPunched = self._custom_punch

        self._original_init = bsSpaz.Spaz.__init__
        bsSpaz.Spaz.__init__ = self._custom_init

    def _custom_init(self, *args, **kwargs):
        self._original_init(self, *args, **kwargs)
        try:
            self.node.damageMultiplier *= 0.5
            self.node.throwStrength *= 1.5
        except Exception as e:
            print("خطا در کاهش دمیج یا پرتاب:", e)

    def _custom_punch(self, puncher, punchType='default'):
        try:
            puncher.node.hurtMagnitude *= 2.0
            if puncher._lastPunched is not None and hasattr(puncher._lastPunched, 'node'):
                victim = puncher._lastPunched
                if victim.node.exists():
                    vel = victim.node.velocity
                    victim.node.velocity = (vel[0]*2, vel[1]*2, vel[2]*2)
                    victim.handleMessage(bs.DieMessage(how='punch'))
        except Exception as e:
            print("خطا در مشت:", e)

        return self._original_punch(puncher, punchType)
