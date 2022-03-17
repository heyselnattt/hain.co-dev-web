export interface IReceivedProduct {
    productId: string;
    productName: string;
    productPrice: number;
    productImageLink: string;
    productStock: number;
    productDescription: string;
    productType: ProductType;
    productIsActive: boolean;
}

export interface IProduct {
    productName: string;
    productPrice: number;
    productImageLink: string;
    productStock: number;
    productDescription: string;
    productType: ProductType;
    productIsActive: boolean;
}

export enum ProductType {
    BREAKFAST = 1,
    LUNCH,
    DESSERT,
    EXTRA
}