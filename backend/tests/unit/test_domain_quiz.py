import pytest
from app.domain.quiz import Quiz, QuizFrage


def test_quizfrage_erstellen():
    frage = QuizFrage(
        frage="Was ist Clean Architecture?",
        antworten=["Ein Muster", "Eine Sprache", "Ein Framework"],
        richtige_antwort=0,
    )
    assert frage.frage == "Was ist Clean Architecture?"
    assert len(frage.antworten) == 3
    assert frage.richtige_antwort == 0


def test_quizfrage_zu_wenig_antworten():
    with pytest.raises(ValueError, match="Mindestens 2"):
        QuizFrage(frage="Frage?", antworten=["Nur eine"], richtige_antwort=0)


def test_quizfrage_ungültiger_index():
    with pytest.raises(ValueError, match="gültiger Index"):
        QuizFrage(frage="Frage?", antworten=["A", "B"], richtige_antwort=5)


def test_quiz_erstellen():
    quiz = Quiz(title="Python Quiz", document_id=1)
    assert quiz.title == "Python Quiz"
    assert quiz.fragen == []
