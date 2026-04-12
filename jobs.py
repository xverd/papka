from data import db_session
from data.jobs import Job
import datetime


def main():
    db_session.global_init('db/mars.db')
    db_sess = db_session.create_session()

    db_sess.add(Job(
        team_leader=1,
        job='deployment of residential modules 1 and 2',
        work_size=15,
        collaborators='2, 3',
        start_date=datetime.datetime.now(),
        is_finished=False
    ))
    db_sess.commit()


if __name__ == '__main__':
    main()