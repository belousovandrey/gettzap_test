from selenium.webdriver.common.by import By


class MainPageLocators:
    REGIONS_BUTTON = (By.CSS_SELECTOR, '[class="MuiBackdrop-root geo-tooltip__backdrop MuiBackdrop-invisible"]')
    COOKIE_BUTTON = (By.CSS_SELECTOR, '[class="MuiButtonBase-root MuiIconButton-root icon-button__root icon-button__root_size_default cookies-notification__button"]')
    # login_form
    MAIN_LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="MuiButtonBase-root MuiButton-root MuiButton-outlined customer-header-login__button-initial"]')
    LOGIN = (By.CSS_SELECTOR, '[class="MuiInputBase-input MuiInput-input text-field__input"]')
    PASSWORD = (By.CSS_SELECTOR, '[class="MuiInputBase-input MuiInput-input text-field__input password-input__input MuiInputBase-inputAdornedEnd"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary"]')
    LOGIN_ERROR = (By.CSS_SELECTOR, '[class="MuiFormHelperText-root Mui-error MuiFormHelperText-filled"]')
    # registration_form
    REG_USER_BUTTON = (By.CSS_SELECTOR, 'body > div.MuiDialog-root > div.MuiDialog-container.auth-dialog__dialog-container.MuiDialog-scrollPaper > div > div.dialog__content.auth-dialog__dialog-content > div.MuiFormControl-root.MuiFormControl-marginNormal.MuiFormControl-fullWidth > p:nth-child(2) > button')
    REG_COMPANY_BUTTON = (By.CSS_SELECTOR, 'body > div.MuiDialog-root > div.MuiDialog-container.auth-dialog__dialog-container.MuiDialog-scrollPaper > div > div.dialog__content.auth-dialog__dialog-content > div.MuiFormControl-root.MuiFormControl-marginNormal.MuiFormControl-fullWidth > p:nth-child(3) > button')
    FIO_USER = (By.CSS_SELECTOR, 'body > div.MuiDialog-root > div.MuiDialog-container.auth-dialog__dialog-container.MuiDialog-scrollPaper > div > div.dialog__content.auth-dialog__dialog-content > form > div.signup__inputs-slot > div:nth-child(1) > div > input')
    PHONE_USER = (By.CSS_SELECTOR, 'body > div.MuiDialog-root > div.MuiDialog-container.auth-dialog__dialog-container.MuiDialog-scrollPaper > div > div.dialog__content.auth-dialog__dialog-content > form > div.signup__inputs-slot > div:nth-child(2) > div > input')
    EMAIL_USER = (By.CSS_SELECTOR, 'body > div.MuiDialog-root > div.MuiDialog-container.auth-dialog__dialog-container.MuiDialog-scrollPaper > div > div.dialog__content.auth-dialog__dialog-content > form > div.signup__inputs-slot > div:nth-child(3) > div > input')
    AGREEMENT_BOX = (By.CSS_SELECTOR, 'body > div.MuiDialog-root > div.MuiDialog-container.auth-dialog__dialog-container.MuiDialog-scrollPaper > div > div.dialog__content.auth-dialog__dialog-content > label > span.MuiTypography-root.MuiFormControlLabel-label.MuiTypography-body1 > p')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#registration-btn')
    # link
    ORDER_LINK = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/header/div[4]/div/div[1]/div/a')
    ORDER_LINK_BUTTON = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/header/div[4]/div/div[1]/div/a/div/p')
    FAVORITES_LINK = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/header/div[4]/div/div[2]/div/a')
    FAVORITES_LINK_BUTTON = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/header/div[4]/div/div[2]/div/a/div/p')
    # _BUTTON = (By.CSS_SELECTOR, '[class="jss458"]')