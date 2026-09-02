from typing import Dict, Any
from noorvision.evaluation_models import EvaluationOutcome, ExecutionRecord


class RealWorldLogicMetric:
    """
    متریک سنجش استدلال مبتنی بر عقل سلیم و دنیای واقعی در نورویژن.
    این متریک بررسی می‌کند که آیا مدل علاوه بر جواب متنی، باگ‌های ساختاری و تناقضات دنیای واقعی را تشخیص داده است یا خیر.
    """

    def __init__(self, metric_name: str = "real_world_logic"):
        self.metric_name = metric_name

    def evaluate(self, record: ExecutionRecord, expected_keywords: list[str]) -> EvaluationOutcome:
        """
        ارزیابی رکورد اجرا بر اساس وجود کلمات کلیدی تحلیلی در پاسخ مدل.
        """
        output_text = str(record.actual_output).lower()
        
        # بررسی اینکه آیا مدل متوجه تناقض/باگ شده است یا خیر
        matched_keywords = [kw for kw in expected_keywords if kw.lower() in output_text]
        
        # محاسبه نمره: نسبت کلمات کلیدی تحلیلیِ کشف‌شده
        score = len(matched_keywords) / len(expected_keywords) if expected_keywords else 0.0
        passed = score >= 0.5  # اگر حداقل ۵۰٪ نکات تحلیلی را کشف کند قبول می‌شود

        reason = (
            f"Model identified {len(matched_keywords)}/{len(expected_keywords)} real-world nuances."
            if passed else "Model failed to detect real-world contradictions/nuances."
        )

        return EvaluationOutcome(
            case_id=f"case-{record.execution_id}",
            passed=passed,
            score=score,
            reason=reason,
            execution=record,
        )
