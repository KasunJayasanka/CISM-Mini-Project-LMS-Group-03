# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsDepartmenthead(models.Model):
    department = models.ForeignKey('CourseProgram', models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField('AccountsUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_departmenthead'


class AccountsParent(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    relation_ship = models.TextField()
    student = models.OneToOneField('AccountsStudent', models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField('AccountsUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_parent'


class AccountsStudent(models.Model):
    level = models.CharField(max_length=25, blank=True, null=True)
    program = models.ForeignKey('CourseProgram', models.DO_NOTHING, blank=True, null=True)
    student = models.OneToOneField('AccountsUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_student'


class AccountsUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    is_student = models.BooleanField()
    is_lecturer = models.BooleanField()
    is_parent = models.BooleanField()
    is_dep_head = models.BooleanField()
    gender = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AccountsUserGroups(models.Model):
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_groups'
        unique_together = (('user', 'group'),)


class AccountsUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CoreActivitylog(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'core_activitylog'


class CoreNewsandevents(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    posted_as = models.CharField(max_length=10)
    updated_date = models.DateTimeField(blank=True, null=True)
    upload_time = models.DateTimeField(blank=True, null=True)
    summary_en = models.TextField(blank=True, null=True)
    summary_ru = models.TextField(blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_ru = models.CharField(max_length=200, blank=True, null=True)
    summary_es = models.TextField(blank=True, null=True)
    summary_fr = models.TextField(blank=True, null=True)
    title_es = models.CharField(max_length=200, blank=True, null=True)
    title_fr = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_newsandevents'


class CoreSemester(models.Model):
    semester = models.CharField(max_length=10)
    is_current_semester = models.BooleanField(blank=True, null=True)
    next_semester_begins = models.DateField(blank=True, null=True)
    session = models.ForeignKey('CoreSession', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_semester'


class CoreSession(models.Model):
    session = models.CharField(unique=True, max_length=200)
    is_current_session = models.BooleanField(blank=True, null=True)
    next_session_begins = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_session'


class CourseCourse(models.Model):
    slug = models.CharField(unique=True, max_length=50)
    title = models.CharField(max_length=200)
    code = models.CharField(unique=True, max_length=200)
    credit = models.IntegerField()
    summary = models.TextField()
    level = models.CharField(max_length=25)
    semester = models.CharField(max_length=200)
    is_elective = models.BooleanField()
    program = models.ForeignKey('CourseProgram', models.DO_NOTHING)
    summary_en = models.TextField(blank=True, null=True)
    summary_ru = models.TextField(blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_ru = models.CharField(max_length=200, blank=True, null=True)
    summary_es = models.TextField(blank=True, null=True)
    summary_fr = models.TextField(blank=True, null=True)
    title_es = models.CharField(max_length=200, blank=True, null=True)
    title_fr = models.CharField(max_length=200, blank=True, null=True)
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course_course'


class CourseCourseallocation(models.Model):
    lecturer = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    session = models.ForeignKey(CoreSession, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_courseallocation'


class CourseCourseallocationCourses(models.Model):
    courseallocation = models.ForeignKey(CourseCourseallocation, models.DO_NOTHING)
    course = models.ForeignKey(CourseCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'course_courseallocation_courses'
        unique_together = (('courseallocation', 'course'),)


class CourseCourseoffer(models.Model):
    dep_head = models.ForeignKey(AccountsDepartmenthead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'course_courseoffer'


class CourseProgram(models.Model):
    title = models.CharField(unique=True, max_length=150)
    summary_en = models.TextField(blank=True, null=True)
    summary_ru = models.TextField(blank=True, null=True)
    title_en = models.CharField(unique=True, max_length=150, blank=True, null=True)
    title_ru = models.CharField(unique=True, max_length=150, blank=True, null=True)
    summary_es = models.TextField(blank=True, null=True)
    summary_fr = models.TextField(blank=True, null=True)
    title_es = models.CharField(unique=True, max_length=150, blank=True, null=True)
    title_fr = models.CharField(unique=True, max_length=150, blank=True, null=True)
    summary = models.TextField()

    class Meta:
        managed = False
        db_table = 'course_program'


class CourseUpload(models.Model):
    title = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    updated_date = models.DateTimeField()
    course = models.ForeignKey(CourseCourse, models.DO_NOTHING)
    title_en = models.CharField(max_length=100, blank=True, null=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    title_es = models.CharField(max_length=100, blank=True, null=True)
    title_fr = models.CharField(max_length=100, blank=True, null=True)
    upload_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'course_upload'


class CourseUploadvideo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=50)
    video = models.CharField(max_length=100)
    summary = models.TextField()
    course = models.ForeignKey(CourseCourse, models.DO_NOTHING)
    summary_en = models.TextField(blank=True, null=True)
    summary_ru = models.TextField(blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    summary_es = models.TextField(blank=True, null=True)
    summary_fr = models.TextField(blank=True, null=True)
    title_es = models.CharField(max_length=100, blank=True, null=True)
    title_fr = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'course_uploadvideo'


class DashboardUserdashboardmodule(models.Model):
    title = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    app_label = models.CharField(max_length=255, blank=True, null=True)
    column = models.PositiveIntegerField()
    order = models.IntegerField()
    settings = models.TextField()
    children = models.TextField()
    collapsed = models.BooleanField()
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dashboard_userdashboardmodule'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class JetBookmark(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING, blank=True, null=True)
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jet_bookmark'


class JetPinnedapplication(models.Model):
    app_label = models.CharField(max_length=255)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING, blank=True, null=True)
    date_add = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jet_pinnedapplication'


class PaymentsInvoice(models.Model):
    total = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment_complete = models.BooleanField()
    invoice_code = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payments_invoice'


class QuizChoice(models.Model):
    choice_text = models.CharField(max_length=1000)
    correct = models.BooleanField()
    question = models.ForeignKey('QuizMcquestion', models.DO_NOTHING)
    choice_text_en = models.CharField(max_length=1000, blank=True, null=True)
    choice_text_ru = models.CharField(max_length=1000, blank=True, null=True)
    choice_text_es = models.CharField(max_length=1000, blank=True, null=True)
    choice_text_fr = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz_choice'


class QuizEssayquestion(models.Model):
    question_ptr = models.OneToOneField('QuizQuestion', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'quiz_essayquestion'


class QuizMcquestion(models.Model):
    question_ptr = models.OneToOneField('QuizQuestion', models.DO_NOTHING, primary_key=True)
    choice_order = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'quiz_mcquestion'


class QuizProgress(models.Model):
    score = models.CharField(max_length=1024)
    user = models.OneToOneField(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quiz_progress'


class QuizQuestion(models.Model):
    content = models.CharField(max_length=1000)
    explanation = models.TextField()
    content_en = models.CharField(max_length=1000, blank=True, null=True)
    content_ru = models.CharField(max_length=1000, blank=True, null=True)
    explanation_en = models.TextField(blank=True, null=True)
    explanation_ru = models.TextField(blank=True, null=True)
    content_es = models.CharField(max_length=1000, blank=True, null=True)
    content_fr = models.CharField(max_length=1000, blank=True, null=True)
    explanation_es = models.TextField(blank=True, null=True)
    explanation_fr = models.TextField(blank=True, null=True)
    figure = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'quiz_question'


class QuizQuestionQuiz(models.Model):
    question = models.ForeignKey(QuizQuestion, models.DO_NOTHING)
    quiz = models.ForeignKey('QuizQuiz', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quiz_question_quiz'
        unique_together = (('question', 'quiz'),)


class QuizQuiz(models.Model):
    title = models.CharField(max_length=60)
    slug = models.CharField(unique=True, max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=20)
    random_order = models.BooleanField()
    answers_at_end = models.BooleanField()
    exam_paper = models.BooleanField()
    single_attempt = models.BooleanField()
    pass_mark = models.SmallIntegerField()
    draft = models.BooleanField()
    timestamp = models.DateTimeField()
    description_en = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    title_en = models.CharField(max_length=60, blank=True, null=True)
    title_ru = models.CharField(max_length=60, blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    title_es = models.CharField(max_length=60, blank=True, null=True)
    title_fr = models.CharField(max_length=60, blank=True, null=True)
    course = models.ForeignKey(CourseCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quiz_quiz'


class QuizSitting(models.Model):
    question_order = models.CharField(max_length=1024)
    question_list = models.CharField(max_length=1024)
    incorrect_questions = models.CharField(max_length=1024)
    current_score = models.IntegerField()
    complete = models.BooleanField()
    user_answers = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    quiz = models.ForeignKey(QuizQuiz, models.DO_NOTHING)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    course = models.ForeignKey(CourseCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quiz_sitting'


class ResultResult(models.Model):
    gpa = models.FloatField(blank=True, null=True)
    cgpa = models.FloatField(blank=True, null=True)
    semester = models.CharField(max_length=100)
    session = models.CharField(max_length=100, blank=True, null=True)
    student = models.ForeignKey(AccountsStudent, models.DO_NOTHING)
    level = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result_result'


class ResultTakencourse(models.Model):
    assignment = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    mid_exam = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    quiz = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    attendance = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    final_exam = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    total = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    grade = models.CharField(max_length=2)
    point = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    comment = models.CharField(max_length=200)
    course = models.ForeignKey(CourseCourse, models.DO_NOTHING)
    student = models.ForeignKey(AccountsStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'result_takencourse'
