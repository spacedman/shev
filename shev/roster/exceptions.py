from django.forms import ValidationError


class BaseValidationError(ValidationError):
    def __init__(self, params=None):
        # If suitable, provide a dict of relevant params
        kwargs = {'params': params} if params and isinstance(params, dict) else {}
        kwargs['code'] = self.code
        super(BaseValidationError, self).__init__(self.message, **kwargs)


class ShiftsOverlapError(BaseValidationError):
    code = 'SHIFT_OVERLAP'
    message = ('You have one or more shifts already scheduled ' +
        'for this person for this time period')
