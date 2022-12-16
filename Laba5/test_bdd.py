from behave import given, when, then
import unique


@given('list of numbers: [{arr}]')
def step(context, arr):
    context.data = [int(elem) for elem in arr.split(', ')]


@given('list of letters: [{arr}]')
def step(context, arr):
    context.data = arr.split(', ')


@when('start Unique iterator')
def step(context):
    context.res = list(unique(context.data))


@when('start Unique iterator + ignore_case')
def step(context):
    context.res = list(unique(context.data, ignore_case=True))


@then('values, numbers [{arr}]')
def step(context, arr):
    assert context.res == [int(i) for i in arr.split(', ')]


@then('values, letters [{arr}]')
def step(context, arr):
    assert sorted(context.res) == sorted(arr.split(', '))