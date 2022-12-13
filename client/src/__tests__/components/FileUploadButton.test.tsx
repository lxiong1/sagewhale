import {render, screen} from '@testing-library/react'
import '@testing-library/jest-dom'
import FileUploadButton from '../../components/FileUploadButton'

test('Should render file upload button', async () => {
    render(<FileUploadButton />)

    expect(screen.getByRole('button')).toHaveTextContent('Upload File')
})
