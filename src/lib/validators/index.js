export default {
    isEmailValid: (/** @type string */ email) => {
        const emailRegexp = new RegExp(
            /^[a-zA-Z0-9][\~\!\$\%\^\&\*_\=\+\}\{\'\?\-\.\\\#\/\`\|]{0,1}([a-zA-Z0-9][\~\!\$\%\^\&\*_\=\+\}\{\'\?\-\.\\\#\/\`\|]{0,1})*[a-zA-Z0-9]@[a-zA-Z0-9][-\.]{0,1}([a-zA-Z][-\.]{0,1})*[a-zA-Z0-9]\.[a-zA-Z0-9]{1,}([\.\-]{0,1}[a-zA-Z]){0,}[a-zA-Z0-9]{0,}$/i
        );
        return emailRegexp.test(email);
    },
    isPassValid: (pass) => {
        const passRegexp = new RegExp(/([a-zA-z0-9!@#$%^&*(),.;'\\_\\]{6,})/)
        return passRegexp.test(pass)
    },
    containsLettersAndCharacters: (text) => {
        let regexp = new RegExp(/[a-zA-Z~!@)(*,.\\#$%^;&*_=+}{'?-]/)
        return regexp.test(text)
    },
    containsUpperCase: (/** @type string */ text) => {
        let upChecker = false;
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").every((c) => {
            if (text.match(c)) {
                upChecker = true;
                return false;
            }
            return true;
        });
        return upChecker;
    },
    containsLowerCase: (/** @type string */ text) => {
        let lowerChecker = false;
        "abcdefghijklmnopqrstuvwxyz".split("").every((c) => {
            if (text.match(c)) {
                lowerChecker = true;
                return false;
            }
            return true;
        });
        return lowerChecker;
    },
    containsDigit: (/** @type string */ text) => {
        let numChecker = false;
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].every((d) => {
            if (text.match(d.toString())) {
                numChecker = true;
                return false;
            }
            return true;
        });
        return numChecker;
    },
    containsSpecialChar: (/** @type string */ text) => {
        let specChecker;
        "~!$%^&*_=+}{'?-".split("").every((sc) => {
            const re = new RegExp(`\\${sc}`);
            if (text.match(re)) {
                specChecker = true;
                return false;
            }
            return true;
        });
        return specChecker;
    },
};
