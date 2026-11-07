from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from enum import Enum

class TipoMovimentacao(Enum):
    ENTRADA = "entrada"
    SAIDA = "saida"

@dataclass
class Movimentacao:
    descricao: str
    valor: Decimal
    tipo: TipoMovimentacao
    categoria: str
    data: date
    id: int | None = None

    def __post_init__(self):

        if not isinstance(self.descricao, str):
            raise TypeError("A descrição deve ser um texto.")

        if not isinstance(self.categoria, str):
            raise TypeError("A categoria deve ser um texto.")
        
        self.descricao = self.descricao.strip()
        self.categoria = self.categoria.strip()

        if not self.descricao:
            raise ValueError("A descrição não pode ficar vazia.")

        if not self.categoria:
            raise ValueError("A categoria não pode ficar vazia.")

        if not isinstance(self.valor, Decimal):
            raise TypeError("O valor deve ser um Decimal.")

        if not self.valor.is_finite() or self.valor <= 0:
            raise ValueError("O valor deve ser positivo e válido.")

        if not isinstance(self.tipo, TipoMovimentacao):
            raise TypeError("O tipo deve ser ENTRADA ou SAIDA.")

        if not isinstance(self.data, date) or isinstance(self.data, datetime):
            raise TypeError("A data deve ser um objeto do tipo date, sem horário.")
        
        if self.id is not None:
            if isinstance(self.id, bool) or not isinstance(self.id, int):
                raise TypeError("O ID deve ser um número inteiro.")

