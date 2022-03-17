export interface IReceivedTransaction {
    transactionId: string;
    transactionDescription: string;
    transactionAgent: string;
    transactionType: TransactionType;
    transactionAmount?: number;
    transactionDate: Date;
}

export interface ITransaction {
    transactionDescription: string;
    transactionAgent: string;
    transactionType: TransactionType;
    transactionAmount?: number;
    transactionDate: Date;
}

export enum TransactionType {
    ORDER = 1,
    BUY,
    ADMIN,
}