#include <stdio.h>
#include <string.h>
#include "dividend.h"
int main() {
    int done = 0;
    struct CompanyInfo company[MAX_COMP];
    initializeInfo(company);
    strcpy(company[0].name, "TC Energy");
    strcpy(company[1].name, "Canadian Utilities");
    strcpy(company[2].name, "Bank of Nova Scotia");
    strcpy(company[3].name, "TransAlta Renewables");
    strcpy(company[4].name, "Toronto Dominion Bank");
    strcpy(company[0].symbol, "TRP.TO");
    strcpy(company[1].symbol, "CU.TO");
    strcpy(company[2].symbol, "BNS.TO");
    strcpy(company[3].symbol, "RNW.TO");
    strcpy(company[4].symbol, "TD.TO");
    company[0].div = 3.24;
    company[1].div = 1.76;
    company[2].div = 3.6;
    company[3].div = 0.94;
    company[4].div = 3.16;
    company[0].stockPrice = 55;
    company[1].stockPrice = 31.7;
    company[2].stockPrice = 70.08;
    company[3].stockPrice = 21.75;
    company[4].stockPrice = 74.81;
    userInput(company);
    for(int i = 0; i < MAX_COMP && done == 0; i++) {
        //userInput(company+i);
        calculateDivYield(company+i);
        companyValue(company+i);
    }
    // Output
    output(company);
    return 0;
}

void initializeInfo(struct CompanyInfo * company) { // initializing struct so it doesn't hold garbage value
    for(int i = 0; i < MAX_COMP; i++) {
        company->name[0] = '\0';
        company->symbol[0] = '\0';
        company->stockPrice = 0;
        company->div = 0;
        company->divYield = 0;
        company->valuation[0] = '\0';
        ++company;
    }
}

void userInput(struct CompanyInfo * company) { // taking user's input
    printf("Enter the Company Name: ");
    scanf("%s", company->name, MAX_STR);
    printf("Enter %s's stock symbol: ", company->name);
    scanf("%s", company->symbol, MAX_STR);
    printf("Enter %s's current stock price: ", company->name);
    scanf("%f", &company->stockPrice);
    printf("Enter %s's annual dividend per share: ", company->name);
    scanf("%lf", &company->div);
}

void calculateDivYield(struct CompanyInfo * company) { // calculating Dividend yield
    if(company->stockPrice >= company->div && company->div > 0) {
        company->divYield = company->div / company->stockPrice * 100;
    }
}

void companyValue(struct CompanyInfo * company) { // Evaluating company's value into 3 categories
    if(company->divYield > 0) {
        if(company->divYield == 5) {
            strcpy(company->valuation, "fully Valued");
        }
        else if(company->divYield > 5) {
            strcpy(company->valuation, "Under Valued");
        }
        else if(company->divYield < 5) {
            strcpy(company->valuation, "Over Valued");
        }
    }
    else {
        strcpy(company->valuation, "ERROR");
    }
}

void output(struct CompanyInfo * company) { // printing out companyinfo into the console
    printf("\n%25s   %7s   %5s   %-8s   %5s   %-15s\n", "COMPANY", "SYMBOL", "PRICE", "DIVIDEND", "YIELD", "VALUATION");
    for(int i = 0; i < MAX_COMP; i++) {
        printf("%25s   %7s   %5.2f   %-8.3f   %5.3lf   %-15s\n", company->name, company->symbol, company->stockPrice, company->div, company->divYield, company->valuation);
        ++company;
    }
} 

void clearInputBUffer() {

}