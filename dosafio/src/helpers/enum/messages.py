from enum import Enum


class ResponsesMessages(Enum):
    GENERIC_EXCEPTION = "OPSS! aconteceu um imprevisto"
    PERSON_NOT_FOUND = "Pessoa informada não encontrada"
    ACCOUNT_NOT_FOUND = "Conta informada não encontrada"
    TRANSACTIONS_NOT_FOUND = "Transações não encontradas"
    INVALID_OPERATION_BLOCKED_ACCOUNT = "A conta informada está bloqueada, é impossivel fazer a transação"
    INVALID_OPERATION_INSUFIENT_BALANCE = "Saldo insuficiente"
    INVALID_OPERATION_INSUFIENT_LIMIT = "Limite de saque alcansado"
