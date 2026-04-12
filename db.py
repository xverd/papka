from data import db_session
from data.users import User


def main():
    db_session.global_init('db/mars.db')
    db_sess = db_session.create_session()

    db_sess.add(User(
        surname='Scott',
        name='Ridley',
        age=21,
        position='captain',
        speciality='research engineer',
        address='module_1',
        email='scott_chief@mars.org'
    ))

    db_sess.add(User(surname='Watney', name='Mark', age=35, position='botanist',
                     speciality='exobiology', address='module_2', email='watney@mars.org'))
    db_sess.add(User(surname='Vogel', name='Alex', age=29, position='chemist',
                     speciality='life support', address='module_2', email='vogel@mars.org'))
    db_sess.add(User(surname='Johanssen', name='Beth', age=31, position='pilot',
                     speciality='navigation', address='module_3', email='johanssen@mars.org'))

    db_sess.commit()


if __name__ == '__main__':
    main()