from behave import given, when, then

@given('that the user is on the Online Calculator webpage')
def step_user_is_on_Online_Calculator_page(context):
    context.Framework.LoadPage()

@when('they enter {number}')
def step_enter_first_number(context, number):
    context.Framework.ClickButton(number)

@when('they click the {button} button')
def step_enter_operation(context, button):
    context.Framework.ClickButton(button)

@then('the result of {result} should be displayed')
def step_verify(context, result):
    assert context.Framework.Verify(result) is True