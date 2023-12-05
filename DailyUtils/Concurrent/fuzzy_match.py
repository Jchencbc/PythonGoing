#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字符串模糊匹配

"""
import typing as t
from rapidfuzz import process, fuzz, distance


fuzz_match_map = {
    # normalized Indel distance
    "ratio": fuzz.ratio,
    # unique and common words between strings using fuzz.ratio
    "token_set_ratio": fuzz.token_set_ratio,
    # quick ratio
    "QRatio": fuzz.QRatio
}

distance_match_map = {
    "Hamming": distance.Hamming.normalized_similarity,
    "Indel": distance.Indel.normalized_similarity,
    "Jaro": distance.Jaro.normalized_similarity,
    "JaroWinkler": distance.JaroWinkler.normalized_similarity,
    "Levenshtein": distance.Levenshtein.normalized_similarity,
    "OSA": distance.OSA.normalized_similarity
}


class FuzzyMatchV2:

    def __init__(self, top_n=5, scoring="Levenshtein"):
        """
        :param top_n: 输出匹配个数
        :param scoring: 匹配算法
        """
        self.top_n = top_n
        self.scorer = fuzz_match_map.get(scoring, distance.Levenshtein.normalized_similarity)
        self._score_percent = scoring in fuzz_match_map  # scorer 返回分值是否为0-100

    def run(self, target: str, candidates: t.Collection[str]) -> t.List[t.Dict[str, t.Any]]:
        """

        :param target: 需要模糊匹配输入的字符串，例：自然分娩
        :param candidates: 待匹配的字符串列表，例：['分娩'，'正常分娩','子宫','多囊肝	']
        :return: list of dict with keys: match_result, match_ratio, blocks
        """
        extracts = process.extract(target, candidates, scorer=self.scorer, limit=self.top_n)
        res = [
            {
                "match_result": name,
                "match_ratio": score / 100 if self._score_percent else score,
                "blocks": distance.Levenshtein.opcodes(target, name).as_matching_blocks()
            }
            for name, score, *_ in extracts
        ]

        return res


if __name__ == '__main__':

    # input
    key_str = '多囊肝病'
    need_key_list = [
        '多囊肝', '肝腺瘤术后史', '多囊肝病史', '肝肿瘤术后', '肝脏术后史', '肝多发囊肿	', '肝大待诊', '肝移植', '肝肋下触及',
        '肝肿大', '肝脏肿大', '肝脂肪浸润', '胆囊壁结晶（请随访）', '肝脏未见明显异常', '脂肪肝', '酒精肝', '肝脏病变'
    ]

    matcher = FuzzyMatchV2(top_n=5)  # 输出个数
    match_list = matcher.run(key_str, set(need_key_list))
    print(match_list)

# EOF
