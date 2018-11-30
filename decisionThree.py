def predict_how_many_books_did_you_read_during_last_12months_(data={}):
    if (data.get('do_you_happen_to_read_any_magazines_or_journals_') is None):
        return 16.6762
    if (data['do_you_happen_to_read_any_magazines_or_journals_'] == 'No'):
        if (data.get('sex') is None):
            return 12.67852
        if (data['sex'] == 'Female'):
            if (data.get('race') is None):
                return 16.22492
            if (data['race'] == 'White'):
                if (data.get('last_book_you_read_you_') is None):
                    return 18.19298
                if (data['last_book_you_read_you_'] == 'Borrowed the book from a library'):
                    if (data.get('age') is None):
                        return 32.96226
                    if (data['age'] > 64):
                        return 59.8
                    if (data['age'] <= 64):
                        return 22.36842
                if (data['last_book_you_read_you_'] != 'Borrowed the book from a library'):
                    return 19.75521
            if (data['race'] != 'White'):
                if (data.get('employement') is None):
                    return 9.26207
                if (data['employement'] == 'Have own business/self-employed'):
                    return 97
                if (data['employement'] != 'Have own business/self-employed'):
                    return 8.65278
        if (data['sex'] == 'Male'):
            return 9.16416
    if (data['do_you_happen_to_read_any_magazines_or_journals_'] != 'No'):
        if (data.get('read_any_e_books_during_last_12months_') is None):
            return 20.17616
        if (data['read_any_e_books_during_last_12months_'] == 'Yes'):
            if (data.get('read_any_printed_books_during_last_12months_') is None):
                return 27.63306
            if (data['read_any_printed_books_during_last_12months_'] == 'Yes'):
                if (data.get('marital_status_') is None):
                    return 28.98226
                if (data['marital_status_'] == 'Single'):
                    if (data.get('age') is None):
                        return 67
                    if (data['age'] > 25):
                        return 96.66667
                    if (data['age'] <= 25):
                        return 22.5
                if (data['marital_status_'] != 'Single'):
                    if (data.get('last_book_you_read_you_') is None):
                        return 28.55605
                    if (data['last_book_you_read_you_'] == 'Borrowed the book from a friend or family member'):
                        return 17.92157
                    if (data['last_book_you_read_you_'] != 'Borrowed the book from a friend or family member'):
                        return 29.92911
            if (data['read_any_printed_books_during_last_12months_'] != 'Yes'):
                return 14.11111
        if (data['read_any_e_books_during_last_12months_'] != 'Yes'):
            if (data.get('age') is None):
                return 18.41758
            if (data['age'] > 63):
                if (data.get('education') is None):
                    return 25.76371
                if (data['education'] == 'High school graduate'):
                    return 16.07273
                if (data['education'] != 'High school graduate'):
                    return 28.69231
            if (data['age'] <= 63):
                return 15.83061