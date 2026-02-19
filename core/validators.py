import magic
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Unsupported file extension.'))

def validate_image_type(value):
    """
    Validates that the uploaded file is a valid image.
    """
    initial_pos = value.tell()
    value.seek(0)
    mime_type = magic.from_buffer(value.read(2048), mime=True)
    value.seek(initial_pos)

    if not mime_type.startswith('image/'):
        raise ValidationError(_('Unsupported file type. Please upload a valid image.'))

def validate_document_type(value):
    """
    Validates that the uploaded file is a valid document or archive.
    Allowed: pdf, docx, doc, xls, xlsx, ppt, pptx, zip, rar, 7zip
    """
    initial_pos = value.tell()
    value.seek(0)
    mime_type = magic.from_buffer(value.read(2048), mime=True)
    value.seek(initial_pos)

    allowed_mimes = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.ms-excel',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-powerpoint',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'application/zip',
        'application/x-rar-compressed',
        'application/x-7z-compressed',
        'application/octet-stream', # Sometimes zips/rars show up as this
    ]

    # strict check might fail for some older formats or varying mime types, 
    # but provides better security.
    
    if mime_type not in allowed_mimes:
         raise ValidationError(_(f'Unsupported file type: {mime_type}. Please upload a valid document or archive.'))

def validate_video_type(value):
    """
    Validates that the uploaded file is a valid video or audio file.
    Allowed: mp4, mkv, wmv, 3gp, f4v, avi, mp3
    """
    initial_pos = value.tell()
    value.seek(0)
    mime_type = magic.from_buffer(value.read(2048), mime=True)
    value.seek(initial_pos)

    allowed_mimes = [
        'video/mp4',
        'video/x-matroska',
        'video/x-ms-wmv',
        'video/3gpp',
        'video/x-flv', # f4v is flash video
        'video/x-msvideo', # avi
        'audio/mpeg', # mp3
        'application/octet-stream',
    ]

    if mime_type not in allowed_mimes and not mime_type.startswith('video/'):
        raise ValidationError(_(f'Unsupported file type: {mime_type}. Please upload a valid video or audio file.'))
