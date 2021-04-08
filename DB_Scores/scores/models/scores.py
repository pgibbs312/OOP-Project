import sqlite3

class Score:
    @staticmethod
    def steralize_field_names():
        return ["name", "score"]
    

    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def to_dict(self):
        return {
            "name": self.name,
            "score": self.score
        }
class ScoreManager:
    def __init__(self):
        self._scores = dict()
    
    @property
    def scores(self):
        return list(self._scores.values())
    
    def add_score(self, score):
        self._scores[score.name] = score
    
    def remove_score(self, score_name):
        for score_name in self._scores:
            del self._scores[score_name]

    def __len__(self):
        return len(self._scores)
    
    def get_scores(self):

        score_dict_list = list()
        for score in self._scores.values():
            score_dict_list.append(score.to_dict())
        return sorted(score_dict_list, key=lambda item: item["score"],reverse=True)
    
    def serialize(self):
        score_dict_list = self.get_scores()
        dict_scores = dict()
        dict_scores["scores"] = score_dict_list
        return dict_scores

    def to_json(self, json_file):
        with open(json_file, 'w') as f:
            json.dump(self.serialize(), f)

    def from_json(self, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
            for item in data['scores']:
                new_score = Score(name=item['name'], score=int(item['score']))
                self.add_score(new_score)



